# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_records.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginRecordsWindow(object):
    def setupUi(self, LoginRecordsWindow):
        LoginRecordsWindow.setObjectName("LoginRecordsWindow")
        LoginRecordsWindow.resize(811, 498)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginRecordsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginRecordsWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableFeatureFrame = QtWidgets.QFrame(self.centralwidget)
        self.tableFeatureFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.tableFeatureFrame.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.tableFeatureFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableFeatureFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableFeatureFrame.setObjectName("tableFeatureFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tableFeatureFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginRecordsSortLabel = QtWidgets.QLabel(self.tableFeatureFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginRecordsSortLabel.sizePolicy().hasHeightForWidth())
        self.loginRecordsSortLabel.setSizePolicy(sizePolicy)
        self.loginRecordsSortLabel.setMinimumSize(QtCore.QSize(55, 30))
        self.loginRecordsSortLabel.setMaximumSize(QtCore.QSize(55, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsSortLabel.setFont(font)
        self.loginRecordsSortLabel.setObjectName("loginRecordsSortLabel")
        self.horizontalLayout_3.addWidget(self.loginRecordsSortLabel)
        self.loginRecordsSortComboBox = QtWidgets.QComboBox(self.tableFeatureFrame)
        self.loginRecordsSortComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.loginRecordsSortComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsSortComboBox.setFont(font)
        self.loginRecordsSortComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.loginRecordsSortComboBox.setFrame(True)
        self.loginRecordsSortComboBox.setObjectName("loginRecordsSortComboBox")
        self.loginRecordsSortComboBox.addItem("")
        self.loginRecordsSortComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.loginRecordsSortComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.yearSpinBox = QtWidgets.QSpinBox(self.tableFeatureFrame)
        self.yearSpinBox.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yearSpinBox.setFont(font)
        self.yearSpinBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.yearSpinBox.setFrame(True)
        self.yearSpinBox.setMinimum(1971)
        self.yearSpinBox.setMaximum(3000)
        self.yearSpinBox.setProperty("value", 2019)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.horizontalLayout_3.addWidget(self.yearSpinBox)
        self.loginRecordsSearchParamComboBox = QtWidgets.QComboBox(self.tableFeatureFrame)
        self.loginRecordsSearchParamComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.loginRecordsSearchParamComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsSearchParamComboBox.setFont(font)
        self.loginRecordsSearchParamComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.loginRecordsSearchParamComboBox.setMaxVisibleItems(3)
        self.loginRecordsSearchParamComboBox.setFrame(True)
        self.loginRecordsSearchParamComboBox.setObjectName("loginRecordsSearchParamComboBox")
        self.loginRecordsSearchParamComboBox.addItem("")
        self.loginRecordsSearchParamComboBox.addItem("")
        self.loginRecordsSearchParamComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.loginRecordsSearchParamComboBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.monthComboBox = QtWidgets.QComboBox(self.tableFeatureFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monthComboBox.sizePolicy().hasHeightForWidth())
        self.monthComboBox.setSizePolicy(sizePolicy)
        self.monthComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.monthComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.monthComboBox.setFont(font)
        self.monthComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.monthComboBox.setObjectName("monthComboBox")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.monthComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.monthComboBox)
        self.loginRecordsSearchField = QtWidgets.QLineEdit(self.tableFeatureFrame)
        self.loginRecordsSearchField.setMinimumSize(QtCore.QSize(0, 30))
        self.loginRecordsSearchField.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsSearchField.setFont(font)
        self.loginRecordsSearchField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.loginRecordsSearchField.setObjectName("loginRecordsSearchField")
        self.horizontalLayout_5.addWidget(self.loginRecordsSearchField)
        self.loginRecordsSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.loginRecordsSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loginRecordsSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.loginRecordsSearchButton.setFont(font)
        self.loginRecordsSearchButton.setStyleSheet("QPushButton#loginRecordsSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loginRecordsSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loginRecordsSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("icons/search_info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginRecordsSearchButton.setIcon(icon1)
        self.loginRecordsSearchButton.setIconSize(QtCore.QSize(25, 25))
        self.loginRecordsSearchButton.setObjectName("loginRecordsSearchButton")
        self.horizontalLayout_5.addWidget(self.loginRecordsSearchButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.loginRecordsFlipTableButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.loginRecordsFlipTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loginRecordsFlipTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsFlipTableButton.setFont(font)
        self.loginRecordsFlipTableButton.setStyleSheet("QPushButton#loginRecordsFlipTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loginRecordsFlipTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loginRecordsFlipTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.resource_path("icons/reverse1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginRecordsFlipTableButton.setIcon(icon2)
        self.loginRecordsFlipTableButton.setIconSize(QtCore.QSize(20, 20))
        self.loginRecordsFlipTableButton.setObjectName("loginRecordsFlipTableButton")
        self.horizontalLayout_3.addWidget(self.loginRecordsFlipTableButton)
        self.loginRecordsLoadTableButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.loginRecordsLoadTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loginRecordsLoadTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginRecordsLoadTableButton.setFont(font)
        self.loginRecordsLoadTableButton.setStyleSheet("QPushButton#loginRecordsLoadTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loginRecordsLoadTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loginRecordsLoadTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.resource_path("icons/reload_.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginRecordsLoadTableButton.setIcon(icon3)
        self.loginRecordsLoadTableButton.setIconSize(QtCore.QSize(20, 20))
        self.loginRecordsLoadTableButton.setObjectName("loginRecordsLoadTableButton")
        self.horizontalLayout_3.addWidget(self.loginRecordsLoadTableButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.tableFeatureFrame)
        self.loginRecordsTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.loginRecordsTableWidget.setFont(font)
        self.loginRecordsTableWidget.setStyleSheet("QTableWidget {\n"
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
        self.loginRecordsTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.loginRecordsTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.loginRecordsTableWidget.setAlternatingRowColors(True)
        self.loginRecordsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.loginRecordsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.loginRecordsTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.loginRecordsTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.loginRecordsTableWidget.setShowGrid(False)
        self.loginRecordsTableWidget.setColumnCount(2)
        self.loginRecordsTableWidget.setObjectName("loginRecordsTableWidget")
        self.loginRecordsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.loginRecordsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.loginRecordsTableWidget.setHorizontalHeaderItem(1, item)
        self.loginRecordsTableWidget.horizontalHeader().setDefaultSectionSize(300)
        self.loginRecordsTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.loginRecordsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.loginRecordsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.loginRecordsTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.loginRecordsTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.loginRecordsTableWidget)
        LoginRecordsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginRecordsWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginRecordsWindow)

    def retranslateUi(self, LoginRecordsWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginRecordsWindow.setWindowTitle(_translate("LoginRecordsWindow", "Login Records"))
        self.loginRecordsSortLabel.setText(_translate("LoginRecordsWindow", "Sort By:"))
        self.loginRecordsSortComboBox.setItemText(0, _translate("LoginRecordsWindow", "Username"))
        self.loginRecordsSortComboBox.setItemText(1, _translate("LoginRecordsWindow", "Login Time"))
        self.loginRecordsSearchParamComboBox.setItemText(0, _translate("LoginRecordsWindow", "Search By:"))
        self.loginRecordsSearchParamComboBox.setItemText(1, _translate("LoginRecordsWindow", "Username"))
        self.loginRecordsSearchParamComboBox.setItemText(2, _translate("LoginRecordsWindow", "Month"))
        self.monthComboBox.setItemText(0, _translate("LoginRecordsWindow", "Jan"))
        self.monthComboBox.setItemText(1, _translate("LoginRecordsWindow", "Feb"))
        self.monthComboBox.setItemText(2, _translate("LoginRecordsWindow", "Mar"))
        self.monthComboBox.setItemText(3, _translate("LoginRecordsWindow", "Apr"))
        self.monthComboBox.setItemText(4, _translate("LoginRecordsWindow", "May"))
        self.monthComboBox.setItemText(5, _translate("LoginRecordsWindow", "Jun"))
        self.monthComboBox.setItemText(6, _translate("LoginRecordsWindow", "Jul"))
        self.monthComboBox.setItemText(7, _translate("LoginRecordsWindow", "Aug"))
        self.monthComboBox.setItemText(8, _translate("LoginRecordsWindow", "Sep"))
        self.monthComboBox.setItemText(9, _translate("LoginRecordsWindow", "Oct"))
        self.monthComboBox.setItemText(10, _translate("LoginRecordsWindow", "Nov"))
        self.monthComboBox.setItemText(11, _translate("LoginRecordsWindow", "Dec"))
        self.loginRecordsSearchField.setPlaceholderText(_translate("LoginRecordsWindow", "Type query here"))
        self.loginRecordsSearchButton.setText(_translate("LoginRecordsWindow", "Search"))
        self.loginRecordsFlipTableButton.setText(_translate("LoginRecordsWindow", "Flip Table"))
        self.loginRecordsLoadTableButton.setText(_translate("LoginRecordsWindow", "Load Table"))
        item = self.loginRecordsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LoginRecordsWindow", "USERNAME"))
        item = self.loginRecordsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LoginRecordsWindow", "LOGIN TIME"))

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

