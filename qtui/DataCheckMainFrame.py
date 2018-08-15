# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataCheckMainFrame.ui'
#
# Created: Tue Jul 17 14:22:13 2018
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DataCheckMainFrame(object):
    def setupUi(self, DataCheckMainFrame):
        DataCheckMainFrame.setObjectName(_fromUtf8("DataCheckMainFrame"))
        DataCheckMainFrame.resize(800, 550)
        self.labelCurrFile = QtGui.QLabel(DataCheckMainFrame)
        self.labelCurrFile.setGeometry(QtCore.QRect(0, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelCurrFile.setFont(font)
        self.labelCurrFile.setObjectName(_fromUtf8("labelCurrFile"))
        self.pbtn_opendir = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_opendir.setGeometry(QtCore.QRect(320, 9, 91, 26))
        self.pbtn_opendir.setObjectName(_fromUtf8("pbtn_opendir"))
        self.cmb_dbselector = QtGui.QComboBox(DataCheckMainFrame)
        self.cmb_dbselector.setGeometry(QtCore.QRect(110, 10, 171, 22))
        self.cmb_dbselector.setObjectName(_fromUtf8("cmb_dbselector"))
        self.pbtn_opengdb = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_opengdb.setGeometry(QtCore.QRect(430, 10, 91, 26))
        self.pbtn_opengdb.setObjectName(_fromUtf8("pbtn_opengdb"))
        self.pbtn_openmdb = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_openmdb.setGeometry(QtCore.QRect(540, 10, 91, 26))
        self.pbtn_openmdb.setObjectName(_fromUtf8("pbtn_openmdb"))
        self.pbtn_openrulefile = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_openrulefile.setGeometry(QtCore.QRect(650, 10, 91, 26))
        self.pbtn_openrulefile.setObjectName(_fromUtf8("pbtn_openrulefile"))
        self.gb_checkbox = QtGui.QGroupBox(DataCheckMainFrame)
        self.gb_checkbox.setGeometry(QtCore.QRect(10, 40, 781, 81))
        self.gb_checkbox.setObjectName(_fromUtf8("gb_checkbox"))
        self.ckb_lyrname = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_lyrname.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.ckb_lyrname.setObjectName(_fromUtf8("ckb_lyrname"))
        self.ckb_lyrname_a = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_lyrname_a.setGeometry(QtCore.QRect(120, 20, 81, 16))
        self.ckb_lyrname_a.setObjectName(_fromUtf8("ckb_lyrname_a"))
        self.ckb_fc_code = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_fc_code.setGeometry(QtCore.QRect(210, 20, 81, 16))
        self.ckb_fc_code.setObjectName(_fromUtf8("ckb_fc_code"))
        self.ckb_fcattr = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_fcattr.setGeometry(QtCore.QRect(290, 20, 81, 16))
        self.ckb_fcattr.setObjectName(_fromUtf8("ckb_fcattr"))
        self.ckb_nullfield = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_nullfield.setGeometry(QtCore.QRect(380, 20, 81, 16))
        self.ckb_nullfield.setObjectName(_fromUtf8("ckb_nullfield"))
        self.ckb_attrrange = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_attrrange.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.ckb_attrrange.setObjectName(_fromUtf8("ckb_attrrange"))
        self.ckb_pointoverlay = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_pointoverlay.setGeometry(QtCore.QRect(210, 50, 81, 16))
        self.ckb_pointoverlay.setObjectName(_fromUtf8("ckb_pointoverlay"))
        self.ckb_lineoverlay = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_lineoverlay.setGeometry(QtCore.QRect(290, 50, 81, 16))
        self.ckb_lineoverlay.setObjectName(_fromUtf8("ckb_lineoverlay"))
        self.ckb_polygonoverlay = QtGui.QCheckBox(self.gb_checkbox)
        self.ckb_polygonoverlay.setGeometry(QtCore.QRect(380, 50, 81, 16))
        self.ckb_polygonoverlay.setObjectName(_fromUtf8("ckb_polygonoverlay"))
        self.label = QtGui.QLabel(self.gb_checkbox)
        self.label.setGeometry(QtCore.QRect(160, 50, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pbtn_docheck = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_docheck.setGeometry(QtCore.QRect(140, 125, 111, 31))
        self.pbtn_docheck.setAutoFillBackground(False)
        self.pbtn_docheck.setStyleSheet(_fromUtf8("font: 75 14pt \"Agency FB\";"))
        self.pbtn_docheck.setObjectName(_fromUtf8("pbtn_docheck"))
        self.pbtn_help = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_help.setGeometry(QtCore.QRect(770, 10, 21, 23))
        self.pbtn_help.setObjectName(_fromUtf8("pbtn_help"))
        self.txtbwr_result = QtGui.QTextBrowser(DataCheckMainFrame)
        self.txtbwr_result.setGeometry(QtCore.QRect(0, 160, 801, 391))
        self.txtbwr_result.setObjectName(_fromUtf8("txtbwr_result"))
        self.pbtn_doexport = QtGui.QPushButton(DataCheckMainFrame)
        self.pbtn_doexport.setGeometry(QtCore.QRect(540, 125, 111, 31))
        self.pbtn_doexport.setAutoFillBackground(False)
        self.pbtn_doexport.setStyleSheet(_fromUtf8("font: 75 14pt \"Agency FB\";"))
        self.pbtn_doexport.setObjectName(_fromUtf8("pbtn_doexport"))
        self.label_status = QtGui.QLabel(DataCheckMainFrame)
        self.label_status.setGeometry(QtCore.QRect(290, 140, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_status.setFont(font)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))

        self.retranslateUi(DataCheckMainFrame)
        QtCore.QMetaObject.connectSlotsByName(DataCheckMainFrame)

    def retranslateUi(self, DataCheckMainFrame):
        DataCheckMainFrame.setWindowTitle(_translate("DataCheckMainFrame", "矢量数据检查工具", None))
        self.labelCurrFile.setText(_translate("DataCheckMainFrame", " 当前数据库文件：", None))
        self.pbtn_opendir.setText(_translate("DataCheckMainFrame", "打开文件夹", None))
        self.pbtn_opengdb.setText(_translate("DataCheckMainFrame", "打开GDB", None))
        self.pbtn_openmdb.setText(_translate("DataCheckMainFrame", "打开MDB", None))
        self.pbtn_openrulefile.setText(_translate("DataCheckMainFrame", "打开检查规则", None))
        self.gb_checkbox.setTitle(_translate("DataCheckMainFrame", "检查项", None))
        self.ckb_lyrname.setText(_translate("DataCheckMainFrame", "数据层名", None))
        self.ckb_lyrname_a.setText(_translate("DataCheckMainFrame", "数据层别名", None))
        self.ckb_fc_code.setText(_translate("DataCheckMainFrame", "要素代码", None))
        self.ckb_fcattr.setText(_translate("DataCheckMainFrame", "要素属性项", None))
        self.ckb_nullfield.setText(_translate("DataCheckMainFrame", "空值字段", None))
        self.ckb_attrrange.setText(_translate("DataCheckMainFrame", "属性值范围", None))
        self.ckb_pointoverlay.setText(_translate("DataCheckMainFrame", "点重合", None))
        self.ckb_lineoverlay.setText(_translate("DataCheckMainFrame", "线重合", None))
        self.ckb_polygonoverlay.setText(_translate("DataCheckMainFrame", "面重合", None))
        self.label.setText(_translate("DataCheckMainFrame", "|", None))
        self.pbtn_docheck.setText(_translate("DataCheckMainFrame", "开始检查", None))
        self.pbtn_help.setText(_translate("DataCheckMainFrame", "H?", None))
        self.pbtn_doexport.setText(_translate("DataCheckMainFrame", "结果导出", None))

