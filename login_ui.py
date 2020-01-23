# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(365, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginMainWindow.sizePolicy().hasHeightForWidth())
        LoginMainWindow.setSizePolicy(sizePolicy)
        LoginMainWindow.setMinimumSize(QtCore.QSize(365, 300))
        LoginMainWindow.setMaximumSize(QtCore.QSize(365, 300))
        font = QtGui.QFont()
        font.setPointSize(8)
        LoginMainWindow.setFont(font)
        LoginMainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginMainWindow.setWindowIcon(icon)
        LoginMainWindow.setWindowOpacity(1.0)
        LoginMainWindow.setStyleSheet("margin:0px;")
        self.centralwidget = QtWidgets.QWidget(LoginMainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(230, 240, 230);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalWidget.setStyleSheet("background-color: rgb(230, 240, 230);")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.horizontalWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalFrame = QtWidgets.QFrame(self.horizontalWidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setStyleSheet("background-color: #63b946;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ffffff;\n"
"background-color: #63b946;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout_3.addWidget(self.horizontalFrame, 1, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 4, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(12)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.horizontalWidget)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.usernameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.label_3 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.horizontalWidget)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_3.addWidget(self.passwordLineEdit)
        self.hideShowPasswordButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.hideShowPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.hideShowPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.hideShowPasswordButton.setFont(font)
        self.hideShowPasswordButton.setStyleSheet("")
        self.hideShowPasswordButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("icons/show.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hideShowPasswordButton.setIcon(icon1)
        self.hideShowPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.hideShowPasswordButton.setCheckable(False)
        self.hideShowPasswordButton.setFlat(True)
        self.hideShowPasswordButton.setObjectName("hideShowPasswordButton")
        self.horizontalLayout_3.addWidget(self.hideShowPasswordButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 50, 0, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 30))
        self.cancelButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton#cancelButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#cancelButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#cancelButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.cancelButton.setDefault(True)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.loginButton = QtWidgets.QPushButton(self.horizontalWidget)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loginButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loginButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loginButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_2.addWidget(self.loginButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.formLayout, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.horizontalWidget, 0, 0, 1, 1)
        LoginMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)
        LoginMainWindow.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        LoginMainWindow.setTabOrder(self.passwordLineEdit, self.hideShowPasswordButton)
        LoginMainWindow.setTabOrder(self.hideShowPasswordButton, self.cancelButton)
        LoginMainWindow.setTabOrder(self.cancelButton, self.loginButton)

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "Login"))
        self.label_4.setText(_translate("LoginMainWindow", "SALES MANAGEMENT SYSTEM"))
        self.label_2.setText(_translate("LoginMainWindow", "USERNAME:"))
        self.label_3.setText(_translate("LoginMainWindow", "PASSWORD:"))
        self.hideShowPasswordButton.setToolTip(_translate("LoginMainWindow", "Show Password"))
        self.cancelButton.setText(_translate("LoginMainWindow", "Cancel"))
        self.loginButton.setText(_translate("LoginMainWindow", "Login"))

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

