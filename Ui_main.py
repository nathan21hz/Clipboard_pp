# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Coding\Clipboard++ PC\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import pyperclip

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 250)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.PB_refresh = QtWidgets.QPushButton(self.centralWidget)
        self.PB_refresh.setGeometry(QtCore.QRect(240, 30, 91, 31))
        self.PB_refresh.setObjectName("PB_refresh")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 201, 211))
        self.listWidget.setObjectName("listWidget")
        self.PB_delete = QtWidgets.QPushButton(self.centralWidget)
        self.PB_delete.setGeometry(QtCore.QRect(240, 150, 91, 31))
        self.PB_delete.setObjectName("PB_delete")
        self.PB_clear = QtWidgets.QPushButton(self.centralWidget)
        self.PB_clear.setGeometry(QtCore.QRect(240, 190, 91, 31))
        self.PB_clear.setObjectName("PB_clear")
        self.PB_get = QtWidgets.QPushButton(self.centralWidget)
        self.PB_get.setGeometry(QtCore.QRect(240, 70, 91, 31))
        self.PB_get.setObjectName("PB_get")
        self.PB_add = QtWidgets.QPushButton(self.centralWidget)
        self.PB_add.setGeometry(QtCore.QRect(240, 110, 91, 31))
        self.PB_add.setObjectName("PB_add")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.PB_refresh.clicked.connect(self.DoFresh)
        self.PB_get.clicked.connect(self.DoGet)
        self.PB_add.clicked.connect(self.DoAdd)
        self.PB_delete.clicked.connect(self.DoDelete)
        self.PB_clear.clicked.connect(self.DoClear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clipboard++"))
        self.PB_refresh.setText(_translate("MainWindow", "刷新"))
        self.PB_delete.setText(_translate("MainWindow", "删除"))
        self.PB_clear.setText(_translate("MainWindow", "清空"))
        self.PB_get.setText(_translate("MainWindow", "获取"))
        self.PB_add.setText(_translate("MainWindow", "添加"))
        
    def DoFresh(self):
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "r", encoding="utf-8")
        s=f.read()
        #print(s)
        f.close()
        self.listWidget.clear()
        text = json.loads(s)
        for t in text:
            self.listWidget.addItem(t)
        return
        
    def DoGet(self):
        a = self.listWidget.currentItem()
        #print(a.text())
        if(a):
            pyperclip.copy(a.text())
        return
        
    def DoAdd(self):
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "r", encoding="utf-8")
        s=f.read()
        #print(s)
        f.close()
        text = json.loads(s)
        add = pyperclip.paste()
        text2 = {add:add}
        text.update(text2)
        #print(text)
        s = json.dumps(text)
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "w", encoding="utf-8")
        f.write(s)
        f.close()
        self.DoFresh()
        return
    
    def DoDelete(self):
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "r", encoding="utf-8")
        s=f.read()
        #print(s)
        f.close()
        text = json.loads(s)
        a = self.listWidget.currentItem()
        #print(a.text())
        if(a):
            del text[a.text()]
        s = json.dumps(text)
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "w", encoding="utf-8")
        f.write(s)
        f.close()
        self.DoFresh()
        return
        
    def DoClear(self):
        f = open("C:/Users/ibm/iCloudDrive/iCloud~is~workflow~my~workflows/clipboard++.json",  "w", encoding="utf-8")
        f.write("{}")
        f.close()
        self.DoFresh()
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

