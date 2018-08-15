# -*- coding: utf-8 -*-

# _*_ 在生成的文件夹中加入site-packages _*_
from site import addsitedir
from sys import executable
from os import path

interpreter = executable
sitepkg = path.dirname(interpreter) + "\\site-packages"
addsitedir(sitepkg)
# _*_ 在生成的文件夹中加入site-packages _*_

import arcpy
import sys, os, random, time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qtui import DataCheckMainFrame
import const
from datacheck import DataCheckManager

const.process_start = u'正在数据检查中……'
const.process_complete = u'数据检查完成，恭喜你！'

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class DcContext(QObject):
    progressSignal = pyqtSignal(str)

    def __init__(self):
        super(DcContext,self).__init__()

        # 声明数据检查管理员
        self.dataCheckManager = DataCheckManager()

        # 检查规则文件
        self.ruleFile = None
        self.result = None

        # 数据库名称、当前数据库路径
        self.dbs = None
        self.dbpath = None
        self.currDb = None

    def _docheck(self):
        time.sleep(1)
        self.result = self.dataCheckManager.check(self.dbpath + self.currDb)
        self.progressSignal.emit(const.process_complete)


    def set_dbfilepath(self,filepath):
        if self.isSingleFile(filepath):
            paths = filepath.rpartition('/')
            self.dbpath = paths[0] + paths[1]
            self.currDb = paths[2]
            self.dbs = [self.currDb]
        else:
            arcpy.env.workspace = filepath
            gdbs = arcpy.ListWorkspaces('*','FileGDB')
            mdbs = arcpy.ListWorkspaces('*','Access')

            for gdb in gdbs:
                print gdb


    def isSingleFile(self,filepath):
        return filepath.endswith('.mdb') or filepath.endswith('.gdb')
        pass


class DcThread(QThread):

    def __init__(self):
        super(DcThread,self).__init__()

    def run(self):
        #无条件退出
        while 1:
                break


class App(QWidget):


    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.ui = DataCheckMainFrame.Ui_DataCheckMainFrame()
        self.ui.setupUi(self)
        print u'打开检查工具'

        #数据检查上下文环境
        self.ctx = DcContext()

        #UI Thread
        self.workthread = DcThread()
        #self.workthread = QThread()
        self.ctx.progressSignal.connect(self.set_statusbar_text)


        # 为信号绑定槽
        self.connect(self.ui.pbtn_openrulefile, SIGNAL(_fromUtf8("clicked()")), self.openCheckRuleFile)
        self.connect(self.ui.pbtn_opendir, SIGNAL(_fromUtf8("clicked()")), self.openFileFolder)
        self.connect(self.ui.pbtn_opengdb, SIGNAL(_fromUtf8("clicked()")), self.openGDB)
        self.connect(self.ui.pbtn_openmdb, SIGNAL(_fromUtf8("clicked()")), self.openMDB)
        self.connect(self.ui.pbtn_docheck, SIGNAL(_fromUtf8("clicked()")), self.doCheck)
        self.connect(self.ui.pbtn_doexport, SIGNAL(_fromUtf8("clicked()")), self.doExport)

    def __del__(self):
        print u'关闭检查工具'

    @pyqtSlot()
    def openCheckRuleFile(self):
        # 打开检查规则文件
        xlsPath = str(QFileDialog.getOpenFileName(self, 'Open file', '', 'Excel(*.xls)'))
        self.ctx.ruleFile = xlsPath
        self.ctx.dataCheckManager.set_rulefile(xlsPath)


    @pyqtSlot()
    def openFileFolder(self):
        #打开文件夹，其中每一个gdb 或者 mdb 文件创建一个DataChecker
        #fileName = QFileDialog.getOpenFileName(self,'Open file','/home')
        filedir = str(QFileDialog.getExistingDirectory()).replace('\\','/')
        print 'filedir', filedir,type(filedir)

        arcpy.env.workspace = filedir
        datasets = arcpy.ListWorkspaces("*", "Access")

        for dataset in datasets:
            print (dataset)

        print ("openfilefolder")


    @pyqtSlot()
    def openGDB(self):
        self.ui.cmb_dbselector.clear()
        # 打开gdb 文件（夹）
        gdbPath = str(QFileDialog.getExistingDirectory()).replace('\\', '/')

        print 'true or false', gdbPath.endswith('gdb')
        print 'filePath', gdbPath, type(gdbPath)
        if gdbPath is None:
            return
        self.ctx.set_dbfilepath(gdbPath)
        self.ui.cmb_dbselector.addItems(self.ctx.dbs)
        print ("openGDB")


    @pyqtSlot()
    def openMDB(self):
        self.ui.cmb_dbselector.clear()

        # 打开 mdb 文件
        mdbPath = str(QFileDialog.getOpenFileName(self,'Open file', '', 'GeoDatabase(*.mdb)'))
        if mdbPath is None:
            return
        self.ctx.set_dbfilepath(mdbPath)
        self.ui.cmb_dbselector.addItems(self.ctx.dbs)
        #print 'filePath', mdbPath, type(mdbPath)


    @pyqtSlot()
    def doCheck(self):
        if self.ctx.ruleFile is None:
            QMessageBox.warning(self, u'警告', u'请先选择检查规则文件！')
            return
        if self.ctx.currDb is None:
            QMessageBox.warning(self, u'警告', u'请先选择检查数据库！')
            return
        self.ui.txtbwr_result.setText('')
        self.ui.label_status.setText(u'正在检查中，请稍后……')

        #self.ctx.moveToThread(self.workthread)

        self.workthread.started.connect(self.ctx._docheck)
        self.workthread.start()
        self.workthread.finished.connect(self.showResult)


    @pyqtSlot()
    def doExport(self):
        # 打开 mdb 文件
        savePath = unicode(QFileDialog.getSaveFileName(self, 'Open file', '', u'TXT文件(*.txt)'), 'utf8')
        saveFile = open(savePath,'w')
        saveFile.write(self.ctx.result.get_results())
        saveFile.close()

    def showResult(self):
        print str(self.ctx.result.get_results())

        self.ui.txtbwr_result.setText(self.ctx.result.get_results())

    def set_statusbar_text(self, text):
        self.ui.label_status.setText(text)


def main():
    # Arcpy 处理业务
    app = QApplication(sys.argv)
    appui = App()
    appui.setWindowFlags(Qt.WindowMinimizeButtonHint)
    appui.setFixedSize(800, 550)
    appui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
