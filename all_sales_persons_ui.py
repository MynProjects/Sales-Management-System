# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_sales_persons.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AllSalesPersonsDialog(object):
    def setupUi(self, AllSalesPersonsDialog):
        AllSalesPersonsDialog.setObjectName("AllSalesPersonsDialog")
        AllSalesPersonsDialog.resize(474, 419)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AllSalesPersonsDialog.setWindowIcon(icon)
        AllSalesPersonsDialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(AllSalesPersonsDialog)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.salesPersonsTableWidget = QtWidgets.QTableWidget(AllSalesPersonsDialog)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.salesPersonsTableWidget.setFont(font)
        self.salesPersonsTableWidget.setStyleSheet("QTableWidget {\n"
"    alternate-background-color: #d9d9d9;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"*::section {\n"
"    background-color: #63b946;\n"
"    color: #ffffff;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"    margin: 1px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: #f2f2f2;\n"
"    border: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #bfbfbf;\n"
"    border: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #f2f2f2;\n"
"    border: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #bfbfbf;\n"
"    border: 0px;\n"
"}\n"
"QScrollBar::button:horizontal {\n"
"    color: #000000;\n"
"    background-color: #d9d9d9;\n"
"    border: 0px;\n"
"}")
        self.salesPersonsTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.salesPersonsTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.salesPersonsTableWidget.setColumnCount(1)
        self.salesPersonsTableWidget.setObjectName("salesPersonsTableWidget")
        self.salesPersonsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesPersonsTableWidget.setHorizontalHeaderItem(0, item)
        self.salesPersonsTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.salesPersonsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.salesPersonsTableWidget, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.loginRecordsButton = QtWidgets.QPushButton(AllSalesPersonsDialog)
        self.loginRecordsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.loginRecordsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsButton.setFont(font)
        self.loginRecordsButton.setStyleSheet("QPushButton#loginRecordsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loginRecordsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loginRecordsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("icons/login_records.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginRecordsButton.setIcon(icon1)
        self.loginRecordsButton.setIconSize(QtCore.QSize(20, 20))
        self.loginRecordsButton.setObjectName("loginRecordsButton")
        self.horizontalLayout.addWidget(self.loginRecordsButton)
        self.refreshButton = QtWidgets.QPushButton(AllSalesPersonsDialog)
        self.refreshButton.setMinimumSize(QtCore.QSize(100, 30))
        self.refreshButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.refreshButton.setFont(font)
        self.refreshButton.setStyleSheet("QPushButton#refreshButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#refreshButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#refreshButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.resource_path("icons/reload_.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon2)
        self.refreshButton.setIconSize(QtCore.QSize(20, 20))
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout.addWidget(self.refreshButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(AllSalesPersonsDialog)
        QtCore.QMetaObject.connectSlotsByName(AllSalesPersonsDialog)

    def retranslateUi(self, AllSalesPersonsDialog):
        _translate = QtCore.QCoreApplication.translate
        AllSalesPersonsDialog.setWindowTitle(_translate("AllSalesPersonsDialog", "All Sales Persons"))
        item = self.salesPersonsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AllSalesPersonsDialog", "SALES PERSONS"))
        self.loginRecordsButton.setText(_translate("AllSalesPersonsDialog", "Login Records"))
        self.refreshButton.setText(_translate("AllSalesPersonsDialog", "Refresh"))

    def resource_path(self, relative_path):  # argument types: String
        """
        This method genrates the relative paths to all the resources used in the application
        including image files, source file, media files and what have you. It is very
        necessary because it preserves the path to the resources after producing the
        executable for the application
        """
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

