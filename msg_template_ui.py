# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_template.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NotifMsgWidget(object):
    def setupUi(self, NotifMsgWidget):
        NotifMsgWidget.setObjectName("NotifMsgWidget")
        NotifMsgWidget.resize(380, 80)
        NotifMsgWidget.setMinimumSize(QtCore.QSize(0, 80))
        NotifMsgWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        NotifMsgWidget.setWindowOpacity(0.0)
        NotifMsgWidget.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(NotifMsgWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(NotifMsgWidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 75))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(230, 240, 230);\n"
"}\n"
"QFrame::hover {\n"
"    border-left: 5px solid #ff8566;\n"
"    border-right: 5px solid #ff8566;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.notifDateTimeLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.notifDateTimeLabel.setFont(font)
        self.notifDateTimeLabel.setStyleSheet("QLabel {\n"
"    color: rgb(0, 96, 128);\n"
"    border: 0px;\n"
"}\n"
"")
        self.notifDateTimeLabel.setText("")
        self.notifDateTimeLabel.setWordWrap(False)
        self.notifDateTimeLabel.setObjectName("notifDateTimeLabel")
        self.gridLayout_2.addWidget(self.notifDateTimeLabel, 0, 0, 1, 1)
        self.deleteMsgFromListButton = QtWidgets.QPushButton(self.frame)
        self.deleteMsgFromListButton.setMinimumSize(QtCore.QSize(40, 30))
        self.deleteMsgFromListButton.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteMsgFromListButton.setFont(font)
        self.deleteMsgFromListButton.setStyleSheet("QPushButton#deleteMsgFromListButton{\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(230, 240, 230);\n"
"}\n"
"QPushButton#deleteMsgFromListButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton#deleteMsgFromListButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.deleteMsgFromListButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteMsgFromListButton.setIcon(icon)
        self.deleteMsgFromListButton.setIconSize(QtCore.QSize(20, 20))
        self.deleteMsgFromListButton.setObjectName("deleteMsgFromListButton")
        self.gridLayout_2.addWidget(self.deleteMsgFromListButton, 0, 1, 1, 1)
        self.notifMsgPreviewLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.notifMsgPreviewLabel.setFont(font)
        self.notifMsgPreviewLabel.setStyleSheet("QLabel {\n"
"    color: #ff8566;\n"
"    border: 0px;\n"
"}\n"
"")
        self.notifMsgPreviewLabel.setText("")
        self.notifMsgPreviewLabel.setScaledContents(True)
        self.notifMsgPreviewLabel.setWordWrap(False)
        self.notifMsgPreviewLabel.setOpenExternalLinks(False)
        self.notifMsgPreviewLabel.setObjectName("notifMsgPreviewLabel")
        self.gridLayout_2.addWidget(self.notifMsgPreviewLabel, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(NotifMsgWidget)
        QtCore.QMetaObject.connectSlotsByName(NotifMsgWidget)

    def retranslateUi(self, NotifMsgWidget):
        _translate = QtCore.QCoreApplication.translate
        NotifMsgWidget.setWindowTitle(_translate("NotifMsgWidget", "Form"))
        self.deleteMsgFromListButton.setToolTip(_translate("NotifMsgWidget", "Delete this notification"))

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

