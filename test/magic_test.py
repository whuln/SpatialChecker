#_*_ coding: utf-8 _*_

import arcpy
import os
arcpy.env.workspace = " D:/project/PyProj/PySpatialChecker/100w.mdb"
#
# datasets = arcpy.ListDatasets()
# #print 'ds',len(datasets)
#
# for ds in datasets:
#     for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
#         fcpath = os.path.join(arcpy.env.workspace, ds, fc)
#         desc = arcpy.Describe(fcpath)
#         #print u'图层路径', fcpath
#         print desc.name
#         print desc.aliasName
#         print desc.shapeType
#
#         break

# class A(object):
#
#     def __init__(self, test):
#         self.test = test
#
# a = A(1)
#
# print dir(a)

# print  "sd" in ["sd",'d']

# from datacheck import DataCheckResutls
#
# r = DataCheckResutls()
#
# print r
# names = [u'SPCTRLP', u'SPGRIDL', u'SPMIDXA', u'WTRIVRL', u'WTFEATA', u'WTFEATL', u'WTLABLP', u'WTFEATP', u'WTLINEL', u'RSDENTP', u'RSBULDA', u'RSBULDP', u'RSBULDL', u'RSOBJTP', u'RSOBJTL', u'RSOBJTA', u'RSLABLP', u'TFRLWYL', u'TFFEATL', u'TFFEATP', u'TFHIWYL', u'TFROADL', u'TFBRDGL', u'TFFEATA', u'TFLABLP', u'PILINEL', u'PILINEP', u'PILABLP', u'BOPRVNA', u'BORDERL', u'BODISTA', u'BOCUNTA', u'BOTOWNA', u'BONRSVA', u'LDCNTRL', u'LDFEATL', u'LDELEVP', u'LDFEATP', u'LDFEATA', u'LDLABLP', u'VGTATNA', u'VGTATNP', u'VGTATNL']
#
# print not u"省级行政区Anno" in names

# class MyTest(object):
#     def __init__(self):
#         pass
#     def __str__(self):
#         return '第三方对方水电费是'.decode('utf-8')
#
# s = MyTest()
# print s


# datasets = arcpy.ListDatasets()
# print 'ds',len(datasets)
#
# for ds in datasets:
#     for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
#         fcpath = os.path.join(arcpy.env.workspace, ds, fc)
#         desc = arcpy.Describe(fcpath)
#         print u'图层路径', fcpath

