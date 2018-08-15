# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time
import random
import threading


class MyObject(QObject):
    def __init__(self):
        super(MyObject, self).__init__()

    #用于更新文本框的信号
    update_text_singal = pyqtSignal(str)

    def work(self):
        while(True):
            time.sleep(2)
            self.update_text_singal.emit("python ln")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.text_area = QTextBrowser()
        self.thread_button = QPushButton('Start threads')
        self.thread_button.clicked.connect(self.dowork)

        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_layout.addWidget(self.text_area)
        central_layout.addWidget(self.thread_button)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def dowork(self):
        self.text_area.clear()
        self.obj = MyObject()
        self.obj.update_text_singal.connect(self.update_text)
        self.mythread = QThread()
        self.obj.moveToThread(self.mythread)
        self.mythread.started.connect(self.obj.work)
        self.mythread.start()

    def update_text(self,text):
        self.text_area.append(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())