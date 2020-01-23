# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daily_graph_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DailyGraphMainWindow(object):
    def setupUi(self, DailyGraphMainWindow):
        DailyGraphMainWindow.setObjectName("DailyGraphMainWindow")
        DailyGraphMainWindow.resize(500, 600)
        DailyGraphMainWindow.setMinimumSize(QtCore.QSize(500, 600))
        DailyGraphMainWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DailyGraphMainWindow.setWindowIcon(icon)
        DailyGraphMainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(DailyGraphMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grossIncomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.grossIncomeLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.grossIncomeLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grossIncomeLabel.setFont(font)
        self.grossIncomeLabel.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;")
        self.grossIncomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.grossIncomeLabel.setObjectName("grossIncomeLabel")
        self.verticalLayout.addWidget(self.grossIncomeLabel)
        self.graphDataTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.graphDataTableWidget.setMinimumSize(QtCore.QSize(490, 0))
        self.graphDataTableWidget.setMaximumSize(QtCore.QSize(490, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.graphDataTableWidget.setFont(font)
        self.graphDataTableWidget.setStyleSheet("QTableWidget {\n"
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
        self.graphDataTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphDataTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphDataTableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphDataTableWidget.setAlternatingRowColors(True)
        self.graphDataTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.graphDataTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.graphDataTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.graphDataTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.graphDataTableWidget.setShowGrid(False)
        self.graphDataTableWidget.setColumnCount(2)
        self.graphDataTableWidget.setObjectName("graphDataTableWidget")
        self.graphDataTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.graphDataTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.graphDataTableWidget.setHorizontalHeaderItem(1, item)
        self.graphDataTableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.graphDataTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.graphDataTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.graphDataTableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.viewGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewGraphButton.setMinimumSize(QtCore.QSize(100, 30))
        self.viewGraphButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.viewGraphButton.setFont(font)
        self.viewGraphButton.setStyleSheet("QPushButton#viewGraphButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton#viewGraphButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#viewGraphButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.viewGraphButton.setObjectName("viewGraphButton")
        self.horizontalLayout.addWidget(self.viewGraphButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DailyGraphMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DailyGraphMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DailyGraphMainWindow)

    def retranslateUi(self, DailyGraphMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DailyGraphMainWindow.setWindowTitle(_translate("DailyGraphMainWindow", "Graph"))
        self.grossIncomeLabel.setText(_translate("DailyGraphMainWindow", "GROSS INCOME"))
        item = self.graphDataTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DailyGraphMainWindow", "DAY"))
        item = self.graphDataTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DailyGraphMainWindow", "INCOME (GH₵)"))
        self.viewGraphButton.setText(_translate("DailyGraphMainWindow", "View"))

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

