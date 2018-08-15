# -*- coding: utf-8 -*-

import os, sys
import arcpy
import const
import xlrd, xlwt
import myutil

reload(sys)
sys.setdefaultencoding('utf-8')

#设置检查规则名称
const.CHECK_LAYER_NAME = 'LayerName'
const.CHECK_ALIAS_NAME = 'AliasName'
const.CHECK_FCODE = 'Fcode'
const.CHECK_FIELDS = 'Fields'
const.CHECK_CODE_FIELD_NAME = 'CodeFieldName'
const.CHECK_NULL_FIELDS = 'NullFieldsChk'
const.CHECK_MINMAX_FIELDS = 'MinMaxFields'
const.CHECK_MINMAX_VALUE = 'MinMaxValue'
const.CHECK_BASE_ON_FIELDS = 'BasedOnFields'
const.CHECK_MIN_DIS = 'MinDisInPoint'

#数据检查规则
class DataCheckRules(object):

    def __init__(self, rulefilepath):
        xlsfile = xlrd.open_workbook(rulefilepath)
        ruleXls = xlsfile.sheets()[0]  # 通过索引顺序获取
        nrows = ruleXls.nrows
        ncols = ruleXls.ncols

        # 定义数据检查规则条目
        self.rule_names = ruleXls.row_values(0)
        for i in range(ncols):
            const[self.rule_names[i]] = i

        #print 'CHECK_CODE_FIELD_NAME', const[const.CHECK_CODE_FIELD_NAME]


        #检查规则列表
        self.ruleList = []

        for i in  range(1, nrows):
            self.ruleList.append( ruleXls.row_values(i))

        self.fcnames = [rule[const[const.CHECK_LAYER_NAME]] for rule in self.ruleList]


    def get_rule_of_layer(self, name):
        return self.ruleList[self.fcnames.index(name)]

    def get_fcnames(self):
            return self.fcnames


    # 数据检查结果
class DataCheckResutls(object):


    def __init__(self):
        self.dbpath = None

        self.lyrNameResult = []
        # self.lyrAliasNameResult = []

        self.lyrCheckResults = []
        pass

    def get_results(self):
        result ='数据库：' + self.dbpath + ', 检查结果\n\n'
        result += "图层名错误：\n\0\0" + "、 ".join(self.lyrNameResult) +'\n\n'
        for layerCr in self.lyrCheckResults:
            result += layerCr.get_results() + '\n'

        for layerCr in self.lyrCheckResults:
            print layerCr.get_results()

        return result

class LayerCheckResult(object):

    def __init__(self):
        self.name = None
        self.aliasNameCr = None
        self.fieldsCr = []
        self.fcodeCr=[]
        self.nullFiledsCr = []
        self.minMaxFieldCr = []

    def get_results(self):
        result ="图层名称：" + str(self.name)  + "\n"
        if self.aliasNameCr is None:
            result += "图层别名检查： 无\n"
        else:
            result += "图层别名检查： " + str(self.aliasNameCr) + "\n"

        result += "缺失字段： " + myutil.print_list_row_col(self.fieldsCr,100) + "\n"
        result += "FCODE检查： \n" + myutil.print_list_row_col(self.fcodeCr,3) + "\n"
        result += "null字段检查： \n" + myutil.print_list_row_col(self.nullFiledsCr,3) + "\n"
        result += "最大/小值检查： \n" + myutil.print_list_row_col(self.minMaxFieldCr,3) + "\n"

        return result


#执行数据检查，输出检查结果
class DataChecker(object):
    def __init__(self):
        self._rules = None


    def set_rulefile(self, filepath):
        self._rules = DataCheckRules(filepath)

        # 准备检查规则
        # 规则1 数据层名检查
        self.lyrNames = self._rules.get_fcnames()
        #print self.lyrNames

        # #规则2 数据层别名检查
        # self.lyrAliasNames = self._rules.get_fcaliasnames()
        # # print self.lyrAliasNames

    #执行检查，返回结果
    def check(self, dbpath):
        #准备检查结果框
        result = DataCheckResutls()

        result.dbpath = dbpath
        print 'dbpath = ',dbpath

        arcpy.env.workspace = dbpath
        #arcpy.env.workspace = 'D:/project/PyProj/PySpatialChecker/100w.mdb'
        datasets = arcpy.ListDatasets()

        for ds in datasets:
            for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
                fcpath = os.path.join(arcpy.env.workspace, ds, fc)

                #取出图层描述文件，检查图层名、图层别名
                desc = arcpy.Describe(fcpath)
                #print u'图层路径', fcpath

                #数据层名检查
                if not self._checkFcName(desc.name):
                    result.lyrNameResult.append(desc.name)
                    #print 'name',result.lyrNameResult
                else:
                    lyrcr = LayerCheckResult()
                    lyrcr.name = desc.name

                    # print lyrcr.name

                    #取出该层检查规则
                    rule = self._rules.get_rule_of_layer(desc.name)
                    # print rule[1]

                    #数据层别名检查
                    aliasname = desc.aliasName
                    if aliasname is None or aliasname == '':
                        aliasname = '空'
                    if desc.aliasName != rule[1]:
                        lyrcr.aliasNameCr = '别名应为：'+ rule[1] + ', 实为： ' + aliasname

                    #print lyrcr.aliasNameCr

                    #字段检查
                    r_fns= rule[3].upper().split(',')
                    fields = arcpy.ListFields(fcpath)

                    field_names = [field.name for field in fields]
                    for r_name in r_fns:
                        if not (r_name in field_names):
                            lyrcr.fieldsCr.append(r_name)

                    #print lyrcr.fieldsCr

                    #字段值检查
                    fcodes = rule[2].split(',')
                    nullFieldsChk = rule[5].split(',')
                    null_check_len = len(nullFieldsChk)
                    minMaxFields = rule[6].split(',')
                    minMaxValues = rule[7].split(',')
                    mm_len = len(minMaxFields)

                    #所有要检查值的字段
                    s_fields = ['OBJECTID']
                    s_fields.extend(nullFieldsChk)

                    if mm_len:
                        for field in minMaxFields:
                            if  field.strip() != '' and not (field in  nullFieldsChk):
                                s_fields.append(field)


                    #print u'检查字段: ---------',s_fields
                    with arcpy.da.SearchCursor(fcpath,s_fields) as cursor:
                        for row in cursor:
                            obj_id = row[0]
                            fcode = row[1]   # 1 - null_check_len

                            # null field check   1 - null field len
                            for i in xrange(1, null_check_len+1):
                                if(row[i] is None):
                                    lyrcr.nullFiledsCr.append('OBJECTID: '+ str(obj_id) + ', null-field: ' + nullFieldsChk[i-1])


                            #检查fcode
                            if not fcode in fcodes:
                                lyrcr.fcodeCr.append('OBJECTID: '+ str(obj_id) +', fcode-error: ' + str(fcode))


                            #最大值最小值检查
                            if mm_len and len(minMaxValues) == 2:
                                if row[-1] < minMaxValues[0] or row[-1] > minMaxValues[1]:
                                    lyrcr.minMaxFieldCr.append(obj_id)


                    # print lyrcr.fcodeCr
                    #检查完成
                    result.lyrCheckResults.append(lyrcr)

        print 'check done!'
        return result


    def _checkFcName(self,name):
        return name in self.lyrNames

    # def _checkFcAliasName(self,name):
    #     return name in self.lyrAliasNames


class DataCheckManager(object):
    _count = 0

    def __init__(self):
        self.__class__._count += 1

        # 数据检查结果缓存 DataCheckResutls
        self._cacheDictResults = {}

        self.checker = DataChecker()

        pass

    def __del__(self):
        self.__class__._count -= 1

    def clear(self):
        self._cacheDictResults.clear()

    def set_rulefile(self, filepath):
        self.checker.set_rulefile(filepath)

    def check(self, dbpath):
        result = None
        if self.has_cache(dbpath):
            result = self.get_result(dbpath)
        else:
            self._cacheDictResults[dbpath] = self.checker.check(dbpath)
            result = self._cacheDictResults[dbpath]
        return result

    def has_cache(self,dbpath):
        return self._cacheDictResults.has_key(dbpath)

    def get_result(self, dbpath):
        return self._cacheDictResults.get(dbpath)

