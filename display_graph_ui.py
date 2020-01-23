# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_graph.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DisplayGraphDialog(object):
    def setupUi(self, DisplayGraphDialog):
        DisplayGraphDialog.setObjectName("DisplayGraphDialog")
        DisplayGraphDialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resource_path("icons/sms_icon64x64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DisplayGraphDialog.setWindowIcon(icon)
        DisplayGraphDialog.setStyleSheet("background-color: rgb(230, 240, 230);")
        self.gridLayout = QtWidgets.QGridLayout(DisplayGraphDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.graphLabel = QtWidgets.QLabel(DisplayGraphDialog)
        self.graphLabel.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.graphLabel.setText("")
        self.graphLabel.setScaledContents(True)
        self.graphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphLabel.setObjectName("graphLabel")
        self.gridLayout.addWidget(self.graphLabel, 0, 0, 1, 1)

        self.retranslateUi(DisplayGraphDialog)
        QtCore.QMetaObject.connectSlotsByName(DisplayGraphDialog)

    def retranslateUi(self, DisplayGraphDialog):
        _translate = QtCore.QCoreApplication.translate
        DisplayGraphDialog.setWindowTitle(_translate("DisplayGraphDialog", "Dialog"))

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

