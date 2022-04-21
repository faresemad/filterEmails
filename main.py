#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from sys import argv
import re
ui, _ = loadUiType("untitled.ui")
class Mainwindow(QMainWindow, ui):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setStyleSheet(open("dark-orange.css").read())
        self.setWindowIcon(QIcon("icon.ico"))
        self.setWindowTitle("Email Filter")
        self.handelBtn()
        
    def handelBtn(self):
        self.pushButton_2.clicked.connect(self.locateFile)
        self.pushButton.clicked.connect(self.extractEmail)
    
    def locateFile(self):
        try:
            save_place = QFileDialog.getOpenFileName(self, "Select a file...")
            text = str(save_place)
            self.name=(text[1:].split(',')[0].replace("'",''))
            self.lineEdit.setText(self.name)
        except:
            pass
    def extractEmail(self):
        #regex extarct email
        self.filename = self.lineEdit_2.text()
        try:
            with open(self.name, 'r') as f:
                x = f.read()
                emails = re.findall(r'[\w\.-]+@[\w\.-]+',x)
                for email in emails:
                    with open(f'{self.filename}.txt','a') as f:
                                f.write(f"{email}\n")
                                f.close()
        except Exception as e:
            print(e)
        # QStatusBar.showMessage(self,"we are done")
        QMessageBox.information(self, "Success", "We Are Done")
        self.lineEdit_2.setText("")
        self.lineEdit.setText("")
try:
    app = QApplication(argv)
    myapp = Mainwindow()
    myapp.show()
    app.exec_()
except:
    pass