# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup_login_setup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartupLoginSetupMainWindow(object):
    def setupUi(self, StartupLoginSetupMainWindow):
        StartupLoginSetupMainWindow.setObjectName("StartupLoginSetupMainWindow")
        StartupLoginSetupMainWindow.resize(400, 380)
        StartupLoginSetupMainWindow.setMinimumSize(QtCore.QSize(400, 380))
        StartupLoginSetupMainWindow.setMaximumSize(QtCore.QSize(400, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StartupLoginSetupMainWindow.setWindowIcon(icon)
        StartupLoginSetupMainWindow.setStyleSheet("background-color: rgb(230, 240, 230);")
        self.centralwidget = QtWidgets.QWidget(StartupLoginSetupMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, -1, 20, -1)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.firmNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firmNameLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.firmNameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmNameLabel.setFont(font)
        self.firmNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.firmNameLabel.setObjectName("firmNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firmNameLabel)
        self.firmNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firmNameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.firmNameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmNameLineEdit.setFont(font)
        self.firmNameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.firmNameLineEdit.setFrame(False)
        self.firmNameLineEdit.setObjectName("firmNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firmNameLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.usernameLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.passwordLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.usernameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.usernameLineEdit.setFrame(False)
        self.usernameLineEdit.setReadOnly(True)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passwordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.passwordLineEdit.setFrame(False)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout.addWidget(self.passwordLineEdit)
        self.hideShowPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.hideShowPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.hideShowPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.hideShowPasswordButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.resource_path("icons/show.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hideShowPasswordButton.setIcon(icon1)
        self.hideShowPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.hideShowPasswordButton.setFlat(True)
        self.hideShowPasswordButton.setObjectName("hideShowPasswordButton")
        self.horizontalLayout.addWidget(self.hideShowPasswordButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
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
        self.proceedButton = QtWidgets.QPushButton(self.centralwidget)
        self.proceedButton.setMinimumSize(QtCore.QSize(0, 30))
        self.proceedButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proceedButton.setFont(font)
        self.proceedButton.setStyleSheet("QPushButton#proceedButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#proceedButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#proceedButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.proceedButton.setDefault(True)
        self.proceedButton.setObjectName("proceedButton")
        self.horizontalLayout_2.addWidget(self.proceedButton)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.firmContactLabel = QtWidgets.QLabel(self.centralwidget)
        self.firmContactLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.firmContactLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmContactLabel.setFont(font)
        self.firmContactLabel.setObjectName("firmContactLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firmContactLabel)
        self.firmContactLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firmContactLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.firmContactLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmContactLineEdit.setFont(font)
        self.firmContactLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.firmContactLineEdit.setObjectName("firmContactLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firmContactLineEdit)
        self.firmAddressLabel = QtWidgets.QLabel(self.centralwidget)
        self.firmAddressLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.firmAddressLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmAddressLabel.setFont(font)
        self.firmAddressLabel.setObjectName("firmAddressLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firmAddressLabel)
        self.firmAddressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.firmAddressLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.firmAddressLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmAddressLineEdit.setFont(font)
        self.firmAddressLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.firmAddressLineEdit.setObjectName("firmAddressLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firmAddressLineEdit)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame.setStyleSheet("background-color: #63b946;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;\n"
"background-color: #63b946;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.gridLayout.addWidget(self.horizontalFrame, 1, 0, 1, 1)
        StartupLoginSetupMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartupLoginSetupMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StartupLoginSetupMainWindow)
        StartupLoginSetupMainWindow.setTabOrder(self.firmNameLineEdit, self.firmContactLineEdit)
        StartupLoginSetupMainWindow.setTabOrder(self.firmContactLineEdit, self.firmAddressLineEdit)
        StartupLoginSetupMainWindow.setTabOrder(self.firmAddressLineEdit, self.usernameLineEdit)
        StartupLoginSetupMainWindow.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        StartupLoginSetupMainWindow.setTabOrder(self.passwordLineEdit, self.hideShowPasswordButton)
        StartupLoginSetupMainWindow.setTabOrder(self.hideShowPasswordButton, self.cancelButton)
        StartupLoginSetupMainWindow.setTabOrder(self.cancelButton, self.proceedButton)

    def retranslateUi(self, StartupLoginSetupMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StartupLoginSetupMainWindow.setWindowTitle(_translate("StartupLoginSetupMainWindow", "Login Setup"))
        self.firmNameLabel.setText(_translate("StartupLoginSetupMainWindow", "Firm Name: "))
        self.usernameLabel.setText(_translate("StartupLoginSetupMainWindow", "Username: "))
        self.passwordLabel.setText(_translate("StartupLoginSetupMainWindow", "Password: "))
        self.usernameLineEdit.setText(_translate("StartupLoginSetupMainWindow", "Admin"))
        self.hideShowPasswordButton.setToolTip(_translate("StartupLoginSetupMainWindow", "Show password"))
        self.cancelButton.setText(_translate("StartupLoginSetupMainWindow", "Cancel"))
        self.proceedButton.setText(_translate("StartupLoginSetupMainWindow", "Proceed"))
        self.firmContactLabel.setText(_translate("StartupLoginSetupMainWindow", "Firm Contact:"))
        self.firmAddressLabel.setText(_translate("StartupLoginSetupMainWindow", "Firm Address:"))
        self.label.setText(_translate("StartupLoginSetupMainWindow", "SETUP ADMIN ACCOUNT"))

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

