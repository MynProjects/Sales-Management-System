# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_items.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AllItemsMainWindow(object):
    def setupUi(self, AllItemsMainWindow):
        AllItemsMainWindow.setObjectName("AllItemsMainWindow")
        AllItemsMainWindow.resize(611, 364)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AllItemsMainWindow.setWindowIcon(icon)
        AllItemsMainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(AllItemsMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.itemSearchField = QtWidgets.QLineEdit(self.frame)
        self.itemSearchField.setMinimumSize(QtCore.QSize(0, 30))
        self.itemSearchField.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.itemSearchField.setFont(font)
        self.itemSearchField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.itemSearchField.setObjectName("itemSearchField")
        self.horizontalLayout_5.addWidget(self.itemSearchField)
        self.itemSearchButton = QtWidgets.QPushButton(self.frame)
        self.itemSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.itemSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.itemSearchButton.setFont(font)
        self.itemSearchButton.setStyleSheet("QPushButton#itemSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#itemSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#itemSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("icons/search_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.itemSearchButton.setIcon(icon1)
        self.itemSearchButton.setIconSize(QtCore.QSize(25, 25))
        self.itemSearchButton.setObjectName("itemSearchButton")
        self.horizontalLayout_5.addWidget(self.itemSearchButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.salesLoadTableButton = QtWidgets.QPushButton(self.frame)
        self.salesLoadTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesLoadTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesLoadTableButton.setFont(font)
        self.salesLoadTableButton.setStyleSheet("QPushButton#salesLoadTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesLoadTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesLoadTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.resource_path("icons/reload_.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesLoadTableButton.setIcon(icon2)
        self.salesLoadTableButton.setIconSize(QtCore.QSize(20, 20))
        self.salesLoadTableButton.setObjectName("salesLoadTableButton")
        self.gridLayout.addWidget(self.salesLoadTableButton, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.itemsTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.itemsTableWidget.setFont(font)
        self.itemsTableWidget.setStyleSheet("QTableWidget {\n"
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
        self.itemsTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.itemsTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.itemsTableWidget.setAlternatingRowColors(True)
        self.itemsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.itemsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.itemsTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.itemsTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.itemsTableWidget.setShowGrid(False)
        self.itemsTableWidget.setCornerButtonEnabled(False)
        self.itemsTableWidget.setObjectName("itemsTableWidget")
        self.itemsTableWidget.setColumnCount(3)
        self.itemsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.itemsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.itemsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.itemsTableWidget.setHorizontalHeaderItem(2, item)
        self.itemsTableWidget.horizontalHeader().setVisible(True)
        self.itemsTableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.itemsTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.itemsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.itemsTableWidget.verticalHeader().setVisible(True)
        self.gridLayout_2.addWidget(self.itemsTableWidget, 1, 0, 1, 1)
        AllItemsMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AllItemsMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AllItemsMainWindow)

    def retranslateUi(self, AllItemsMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AllItemsMainWindow.setWindowTitle(_translate("AllItemsMainWindow", "All Items"))
        self.itemSearchField.setPlaceholderText(_translate("AllItemsMainWindow", "Type item name here"))
        self.itemSearchButton.setText(_translate("AllItemsMainWindow", "Search"))
        self.salesLoadTableButton.setText(_translate("AllItemsMainWindow", "Load Table"))
        item = self.itemsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AllItemsMainWindow", "ITEM DESCRIPTION"))
        item = self.itemsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AllItemsMainWindow", "QUANTITY"))
        item = self.itemsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AllItemsMainWindow", "UNIT PRICE"))

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

