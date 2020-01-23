# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sms_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SMSMainWindow(object):
    def setupUi(self, SMSMainWindow):
        SMSMainWindow.setObjectName("SMSMainWindow")
        SMSMainWindow.resize(955, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/sms_icon64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SMSMainWindow.setWindowIcon(icon)
        SMSMainWindow.setWindowOpacity(1.0)
        SMSMainWindow.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.centralwidget = QtWidgets.QWidget(SMSMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuFrame = QtWidgets.QFrame(self.centralwidget)
        self.menuFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.menuFrame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.menuFrame.setStyleSheet("background-color: #63b946;")
        self.menuFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menuFrame.setObjectName("menuFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.menuFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 5, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.salesMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.salesMenuButton.setMinimumSize(QtCore.QSize(150, 50))
        self.salesMenuButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.salesMenuButton.setFont(font)
        self.salesMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.salesMenuButton.setStyleSheet("QPushButton#salesMenuButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#salesMenuButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#salesMenuButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-top: 5px solid #ff8566;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/sales.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesMenuButton.setIcon(icon1)
        self.salesMenuButton.setIconSize(QtCore.QSize(25, 25))
        self.salesMenuButton.setCheckable(True)
        self.salesMenuButton.setChecked(True)
        self.salesMenuButton.setFlat(False)
        self.salesMenuButton.setObjectName("salesMenuButton")
        self.horizontalLayout.addWidget(self.salesMenuButton)
        self.notifMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.notifMenuButton.setMinimumSize(QtCore.QSize(150, 50))
        self.notifMenuButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.notifMenuButton.setFont(font)
        self.notifMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.notifMenuButton.setStyleSheet("QPushButton#notifMenuButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#notifMenuButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#notifMenuButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-top: 5px solid #ff8566;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/notification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifMenuButton.setIcon(icon2)
        self.notifMenuButton.setIconSize(QtCore.QSize(25, 25))
        self.notifMenuButton.setCheckable(True)
        self.notifMenuButton.setFlat(False)
        self.notifMenuButton.setObjectName("notifMenuButton")
        self.horizontalLayout.addWidget(self.notifMenuButton)
        self.recordsMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.recordsMenuButton.setMinimumSize(QtCore.QSize(150, 50))
        self.recordsMenuButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.recordsMenuButton.setFont(font)
        self.recordsMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.recordsMenuButton.setStyleSheet("QPushButton#recordsMenuButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#recordsMenuButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#recordsMenuButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-top: 5px solid #ff8566;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/records.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recordsMenuButton.setIcon(icon3)
        self.recordsMenuButton.setIconSize(QtCore.QSize(25, 25))
        self.recordsMenuButton.setCheckable(True)
        self.recordsMenuButton.setFlat(False)
        self.recordsMenuButton.setObjectName("recordsMenuButton")
        self.horizontalLayout.addWidget(self.recordsMenuButton)
        self.settingsMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.settingsMenuButton.setMinimumSize(QtCore.QSize(150, 50))
        self.settingsMenuButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.settingsMenuButton.setFont(font)
        self.settingsMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.settingsMenuButton.setStyleSheet("QPushButton#settingsMenuButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#settingsMenuButton:hover{\n"
"    color:  #63b946;\n"
"    background-color:  #ffffff;\n"
"}\n"
"QPushButton#settingsMenuButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-top: 5px solid #ff8566;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsMenuButton.setIcon(icon4)
        self.settingsMenuButton.setIconSize(QtCore.QSize(25, 25))
        self.settingsMenuButton.setCheckable(True)
        self.settingsMenuButton.setDefault(False)
        self.settingsMenuButton.setFlat(False)
        self.settingsMenuButton.setObjectName("settingsMenuButton")
        self.horizontalLayout.addWidget(self.settingsMenuButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setContentsMargins(-1, 9, 0, -1)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem1)
        self.backupMenuAnimLabel = QtWidgets.QLabel(self.menuFrame)
        self.backupMenuAnimLabel.setMinimumSize(QtCore.QSize(50, 30))
        self.backupMenuAnimLabel.setMaximumSize(QtCore.QSize(50, 30))
        self.backupMenuAnimLabel.setStyleSheet("")
        self.backupMenuAnimLabel.setText("")
        self.backupMenuAnimLabel.setScaledContents(True)
        self.backupMenuAnimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backupMenuAnimLabel.setObjectName("backupMenuAnimLabel")
        self.verticalLayout_15.addWidget(self.backupMenuAnimLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.backupMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.backupMenuButton.setMinimumSize(QtCore.QSize(50, 50))
        self.backupMenuButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backupMenuButton.setFont(font)
        self.backupMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.backupMenuButton.setStyleSheet("QPushButton#backupMenuButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#backupMenuButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#backupMenuButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    border: 0px;\n"
"    padding: 2px;\n"
"}")
        self.backupMenuButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/backup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backupMenuButton.setIcon(icon5)
        self.backupMenuButton.setIconSize(QtCore.QSize(32, 32))
        self.backupMenuButton.setObjectName("backupMenuButton")
        self.horizontalLayout.addWidget(self.backupMenuButton)
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.horizontalLayout.addLayout(self.horizontalLayout_54)
        self.logoutMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.logoutMenuButton.setMinimumSize(QtCore.QSize(50, 50))
        self.logoutMenuButton.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.logoutMenuButton.setFont(font)
        self.logoutMenuButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logoutMenuButton.setStyleSheet("QPushButton#logoutMenuButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#logoutMenuButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#logoutMenuButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    border: 0px;\n"
"    padding: 2px;\n"
"}")
        self.logoutMenuButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutMenuButton.setIcon(icon6)
        self.logoutMenuButton.setIconSize(QtCore.QSize(40, 40))
        self.logoutMenuButton.setObjectName("logoutMenuButton")
        self.horizontalLayout.addWidget(self.logoutMenuButton)
        self.verticalLayout.addWidget(self.menuFrame)
        self.contentStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.contentStackedWidget.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.contentStackedWidget.setObjectName("contentStackedWidget")
        self.salesPage = QtWidgets.QWidget()
        self.salesPage.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.salesPage.setObjectName("salesPage")
        self.gridLayout = QtWidgets.QGridLayout(self.salesPage)
        self.gridLayout.setContentsMargins(1, -1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.salesPage)
        self.splitter_3.setStyleSheet("QSplitter::handle {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(99, 174, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QSplitter::handle:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"}")
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setChildrenCollapsible(False)
        self.splitter_3.setObjectName("splitter_3")
        self.widget_3 = QtWidgets.QWidget(self.splitter_3)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_3.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.salesPointScrollArea = QtWidgets.QScrollArea(self.widget_3)
        self.salesPointScrollArea.setMinimumSize(QtCore.QSize(295, 0))
        self.salesPointScrollArea.setMaximumSize(QtCore.QSize(495, 16777215))
        self.salesPointScrollArea.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.salesPointScrollArea.setStyleSheet("QScrollArea {\n"
"    background-color: #bfbfbf;\n"
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
        self.salesPointScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.salesPointScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.salesPointScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.salesPointScrollArea.setWidgetResizable(True)
        self.salesPointScrollArea.setObjectName("salesPointScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 293, 550))
        self.scrollAreaWidgetContents_3.setMinimumSize(QtCore.QSize(280, 0))
        self.scrollAreaWidgetContents_3.setMaximumSize(QtCore.QSize(495, 16777215))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.salesItemLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.salesItemLabel_2.setMinimumSize(QtCore.QSize(0, 30))
        self.salesItemLabel_2.setMaximumSize(QtCore.QSize(35, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesItemLabel_2.setFont(font)
        self.salesItemLabel_2.setStyleSheet("color: rgb(46, 52, 54);")
        self.salesItemLabel_2.setObjectName("salesItemLabel_2")
        self.horizontalLayout_11.addWidget(self.salesItemLabel_2)
        self.salesItemComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.salesItemComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.salesItemComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesItemComboBox.setFont(font)
        self.salesItemComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesItemComboBox.setEditable(True)
        self.salesItemComboBox.setCurrentText("")
        self.salesItemComboBox.setMaxVisibleItems(12)
        self.salesItemComboBox.setObjectName("salesItemComboBox")
        self.horizontalLayout_11.addWidget(self.salesItemComboBox)
        self.salesQtyOfItemsLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.salesQtyOfItemsLabel_2.setMinimumSize(QtCore.QSize(80, 30))
        self.salesQtyOfItemsLabel_2.setMaximumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesQtyOfItemsLabel_2.setFont(font)
        self.salesQtyOfItemsLabel_2.setStyleSheet("color: rgb(46, 52, 54);")
        self.salesQtyOfItemsLabel_2.setObjectName("salesQtyOfItemsLabel_2")
        self.horizontalLayout_11.addWidget(self.salesQtyOfItemsLabel_2)
        self.salesQtyOfItemsSpinBox = QtWidgets.QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.salesQtyOfItemsSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.salesQtyOfItemsSpinBox.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesQtyOfItemsSpinBox.setFont(font)
        self.salesQtyOfItemsSpinBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesQtyOfItemsSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.salesQtyOfItemsSpinBox.setDecimals(0)
        self.salesQtyOfItemsSpinBox.setMinimum(1.0)
        self.salesQtyOfItemsSpinBox.setMaximum(1e+18)
        self.salesQtyOfItemsSpinBox.setProperty("value", 1.0)
        self.salesQtyOfItemsSpinBox.setObjectName("salesQtyOfItemsSpinBox")
        self.horizontalLayout_11.addWidget(self.salesQtyOfItemsSpinBox)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.totalCostForSelectedItemLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalCostForSelectedItemLabel.sizePolicy().hasHeightForWidth())
        self.totalCostForSelectedItemLabel.setSizePolicy(sizePolicy)
        self.totalCostForSelectedItemLabel.setMinimumSize(QtCore.QSize(106, 30))
        self.totalCostForSelectedItemLabel.setMaximumSize(QtCore.QSize(106, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalCostForSelectedItemLabel.setFont(font)
        self.totalCostForSelectedItemLabel.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.totalCostForSelectedItemLabel.setObjectName("totalCostForSelectedItemLabel")
        self.horizontalLayout_17.addWidget(self.totalCostForSelectedItemLabel)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setMinimumSize(QtCore.QSize(16, 30))
        self.label_9.setMaximumSize(QtCore.QSize(16, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_17.addWidget(self.label_9)
        self.ghanaCediSymboLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ghanaCediSymboLineEdit.setMinimumSize(QtCore.QSize(32, 30))
        self.ghanaCediSymboLineEdit.setMaximumSize(QtCore.QSize(35, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ghanaCediSymboLineEdit.setFont(font)
        self.ghanaCediSymboLineEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.ghanaCediSymboLineEdit.setFrame(False)
        self.ghanaCediSymboLineEdit.setReadOnly(True)
        self.ghanaCediSymboLineEdit.setObjectName("ghanaCediSymboLineEdit")
        self.horizontalLayout_17.addWidget(self.ghanaCediSymboLineEdit)
        self.totalCostForSelectedItemLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.totalCostForSelectedItemLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.totalCostForSelectedItemLineEdit.setFont(font)
        self.totalCostForSelectedItemLineEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.totalCostForSelectedItemLineEdit.setFrame(False)
        self.totalCostForSelectedItemLineEdit.setReadOnly(True)
        self.totalCostForSelectedItemLineEdit.setObjectName("totalCostForSelectedItemLineEdit")
        self.horizontalLayout_17.addWidget(self.totalCostForSelectedItemLineEdit)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.qtyLeftLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtyLeftLabel.sizePolicy().hasHeightForWidth())
        self.qtyLeftLabel.setSizePolicy(sizePolicy)
        self.qtyLeftLabel.setMinimumSize(QtCore.QSize(106, 30))
        self.qtyLeftLabel.setMaximumSize(QtCore.QSize(106, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.qtyLeftLabel.setFont(font)
        self.qtyLeftLabel.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.qtyLeftLabel.setObjectName("qtyLeftLabel")
        self.horizontalLayout_23.addWidget(self.qtyLeftLabel)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setMinimumSize(QtCore.QSize(16, 30))
        self.label_12.setMaximumSize(QtCore.QSize(16, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_23.addWidget(self.label_12)
        self.itemQtyLeftLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.itemQtyLeftLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.itemQtyLeftLineEdit.setFont(font)
        self.itemQtyLeftLineEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.itemQtyLeftLineEdit.setFrame(False)
        self.itemQtyLeftLineEdit.setReadOnly(True)
        self.itemQtyLeftLineEdit.setObjectName("itemQtyLeftLineEdit")
        self.horizontalLayout_23.addWidget(self.itemQtyLeftLineEdit)
        self.verticalLayout_12.addLayout(self.horizontalLayout_23)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setMinimumSize(QtCore.QSize(0, 20))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_11.addWidget(self.line_2)
        self.addToCartButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.addToCartButton.setMinimumSize(QtCore.QSize(0, 30))
        self.addToCartButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addToCartButton.setFont(font)
        self.addToCartButton.setStyleSheet("QPushButton#addToCartButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"    border-radius: 10px 0px 10px 0px;\n"
"    }\n"
"QPushButton#addToCartButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addToCartButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/_cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addToCartButton.setIcon(icon7)
        self.addToCartButton.setIconSize(QtCore.QSize(30, 30))
        self.addToCartButton.setObjectName("addToCartButton")
        self.verticalLayout_11.addWidget(self.addToCartButton)
        self.cartTableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.cartTableWidget.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cartTableWidget.setFont(font)
        self.cartTableWidget.setStyleSheet("QTableWidget {\n"
"    alternate-background-color: #d9d9d9;\n"
"    background-color: rgb(255, 255, 255);\n"
"    margin-top: 2px;\n"
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
        self.cartTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.cartTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cartTableWidget.setAlternatingRowColors(True)
        self.cartTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.cartTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.cartTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cartTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.cartTableWidget.setShowGrid(False)
        self.cartTableWidget.setCornerButtonEnabled(False)
        self.cartTableWidget.setObjectName("cartTableWidget")
        self.cartTableWidget.setColumnCount(3)
        self.cartTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(3, 3, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.cartTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.cartTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cartTableWidget.setHorizontalHeaderItem(2, item)
        self.cartTableWidget.horizontalHeader().setStretchLastSection(True)
        self.cartTableWidget.verticalHeader().setVisible(False)
        self.cartTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.cartTableWidget)
        self.removeFromCartButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.removeFromCartButton.setMinimumSize(QtCore.QSize(0, 30))
        self.removeFromCartButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeFromCartButton.setFont(font)
        self.removeFromCartButton.setStyleSheet("QPushButton#removeFromCartButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"\n"
"}\n"
"QPushButton#removeFromCartButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#removeFromCartButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeFromCartButton.setIcon(icon8)
        self.removeFromCartButton.setIconSize(QtCore.QSize(20, 20))
        self.removeFromCartButton.setObjectName("removeFromCartButton")
        self.verticalLayout_11.addWidget(self.removeFromCartButton)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.salesTotalCostLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.salesTotalCostLabel.setMinimumSize(QtCore.QSize(90, 30))
        self.salesTotalCostLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesTotalCostLabel.setFont(font)
        self.salesTotalCostLabel.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesTotalCostLabel.setObjectName("salesTotalCostLabel")
        self.horizontalLayout_24.addWidget(self.salesTotalCostLabel)
        self.salesGhanaCediSymboLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.salesGhanaCediSymboLineEdit.setEnabled(False)
        self.salesGhanaCediSymboLineEdit.setMinimumSize(QtCore.QSize(35, 30))
        self.salesGhanaCediSymboLineEdit.setMaximumSize(QtCore.QSize(35, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesGhanaCediSymboLineEdit.setFont(font)
        self.salesGhanaCediSymboLineEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesGhanaCediSymboLineEdit.setFrame(False)
        self.salesGhanaCediSymboLineEdit.setReadOnly(True)
        self.salesGhanaCediSymboLineEdit.setObjectName("salesGhanaCediSymboLineEdit")
        self.horizontalLayout_24.addWidget(self.salesGhanaCediSymboLineEdit)
        self.salesTotalCostLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.salesTotalCostLineEdit.setEnabled(False)
        self.salesTotalCostLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.salesTotalCostLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesTotalCostLineEdit.setFont(font)
        self.salesTotalCostLineEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesTotalCostLineEdit.setFrame(False)
        self.salesTotalCostLineEdit.setReadOnly(True)
        self.salesTotalCostLineEdit.setObjectName("salesTotalCostLineEdit")
        self.horizontalLayout_24.addWidget(self.salesTotalCostLineEdit)
        self.verticalLayout_11.addLayout(self.horizontalLayout_24)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_11)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.salesPointScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.salesPointScrollArea)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.reloadItemsButton = QtWidgets.QPushButton(self.widget_3)
        self.reloadItemsButton.setMinimumSize(QtCore.QSize(0, 30))
        self.reloadItemsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reloadItemsButton.setFont(font)
        self.reloadItemsButton.setStyleSheet("QPushButton#reloadItemsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#reloadItemsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#reloadItemsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/reload_items.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadItemsButton.setIcon(icon9)
        self.reloadItemsButton.setIconSize(QtCore.QSize(20, 20))
        self.reloadItemsButton.setObjectName("reloadItemsButton")
        self.horizontalLayout_7.addWidget(self.reloadItemsButton)
        self.sellButton = QtWidgets.QPushButton(self.widget_3)
        self.sellButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sellButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sellButton.setFont(font)
        self.sellButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sellButton.setStyleSheet("QPushButton#sellButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#sellButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#sellButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/sell.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sellButton.setIcon(icon10)
        self.sellButton.setIconSize(QtCore.QSize(20, 20))
        self.sellButton.setAutoDefault(True)
        self.sellButton.setFlat(False)
        self.sellButton.setObjectName("sellButton")
        self.horizontalLayout_7.addWidget(self.sellButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(6, 0, 6, 9)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.salesResetAllButton = QtWidgets.QPushButton(self.widget_3)
        self.salesResetAllButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesResetAllButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesResetAllButton.setFont(font)
        self.salesResetAllButton.setStyleSheet("QPushButton#salesResetAllButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesResetAllButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesResetAllButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesResetAllButton.setIcon(icon11)
        self.salesResetAllButton.setIconSize(QtCore.QSize(20, 20))
        self.salesResetAllButton.setAutoDefault(True)
        self.salesResetAllButton.setObjectName("salesResetAllButton")
        self.horizontalLayout_8.addWidget(self.salesResetAllButton)
        self.salesPrintReceiptButton = QtWidgets.QPushButton(self.widget_3)
        self.salesPrintReceiptButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesPrintReceiptButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesPrintReceiptButton.setFont(font)
        self.salesPrintReceiptButton.setStyleSheet("QPushButton#salesPrintReceiptButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesPrintReceiptButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesPrintReceiptButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesPrintReceiptButton.setIcon(icon12)
        self.salesPrintReceiptButton.setIconSize(QtCore.QSize(20, 20))
        self.salesPrintReceiptButton.setAutoDefault(True)
        self.salesPrintReceiptButton.setObjectName("salesPrintReceiptButton")
        self.horizontalLayout_8.addWidget(self.salesPrintReceiptButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.widget_6 = QtWidgets.QWidget(self.splitter_3)
        self.widget_6.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableFeatureFrame = QtWidgets.QFrame(self.widget_6)
        self.tableFeatureFrame.setMinimumSize(QtCore.QSize(0, 100))
        self.tableFeatureFrame.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.tableFeatureFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableFeatureFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableFeatureFrame.setObjectName("tableFeatureFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tableFeatureFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.salesSearchDateEdit = QtWidgets.QDateEdit(self.tableFeatureFrame)
        self.salesSearchDateEdit.setEnabled(False)
        self.salesSearchDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.salesSearchDateEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesSearchDateEdit.setFont(font)
        self.salesSearchDateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(46, 52, 54);\n"
"")
        self.salesSearchDateEdit.setFrame(False)
        self.salesSearchDateEdit.setReadOnly(False)
        self.salesSearchDateEdit.setTime(QtCore.QTime(0, 0, 0))
        self.salesSearchDateEdit.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.salesSearchDateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.salesSearchDateEdit.setCalendarPopup(True)
        self.salesSearchDateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.salesSearchDateEdit.setObjectName("salesSearchDateEdit")
        self.horizontalLayout_3.addWidget(self.salesSearchDateEdit)
        self.salesSearchParamComboBox = QtWidgets.QComboBox(self.tableFeatureFrame)
        self.salesSearchParamComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.salesSearchParamComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesSearchParamComboBox.setFont(font)
        self.salesSearchParamComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.salesSearchParamComboBox.setMaxVisibleItems(3)
        self.salesSearchParamComboBox.setFrame(True)
        self.salesSearchParamComboBox.setObjectName("salesSearchParamComboBox")
        self.salesSearchParamComboBox.addItem("")
        self.salesSearchParamComboBox.addItem("")
        self.salesSearchParamComboBox.addItem("")
        self.salesSearchParamComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.salesSearchParamComboBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.salesSearchField = QtWidgets.QLineEdit(self.tableFeatureFrame)
        self.salesSearchField.setMinimumSize(QtCore.QSize(0, 30))
        self.salesSearchField.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesSearchField.setFont(font)
        self.salesSearchField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.salesSearchField.setObjectName("salesSearchField")
        self.horizontalLayout_5.addWidget(self.salesSearchField)
        self.salesSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.salesSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.salesSearchButton.setFont(font)
        self.salesSearchButton.setStyleSheet("QPushButton#salesSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/search_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesSearchButton.setIcon(icon13)
        self.salesSearchButton.setIconSize(QtCore.QSize(25, 25))
        self.salesSearchButton.setObjectName("salesSearchButton")
        self.horizontalLayout_5.addWidget(self.salesSearchButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.salesSortLabel = QtWidgets.QLabel(self.tableFeatureFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.salesSortLabel.sizePolicy().hasHeightForWidth())
        self.salesSortLabel.setSizePolicy(sizePolicy)
        self.salesSortLabel.setMinimumSize(QtCore.QSize(55, 30))
        self.salesSortLabel.setMaximumSize(QtCore.QSize(55, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesSortLabel.setFont(font)
        self.salesSortLabel.setObjectName("salesSortLabel")
        self.horizontalLayout_4.addWidget(self.salesSortLabel)
        self.salesSortComboBox = QtWidgets.QComboBox(self.tableFeatureFrame)
        self.salesSortComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.salesSortComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesSortComboBox.setFont(font)
        self.salesSortComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.salesSortComboBox.setObjectName("salesSortComboBox")
        self.salesSortComboBox.addItem("")
        self.salesSortComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.salesSortComboBox)
        self.salesFlipTableButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.salesFlipTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesFlipTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesFlipTableButton.setFont(font)
        self.salesFlipTableButton.setStyleSheet("QPushButton#salesFlipTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesFlipTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesFlipTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/reverse1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesFlipTableButton.setIcon(icon14)
        self.salesFlipTableButton.setIconSize(QtCore.QSize(20, 20))
        self.salesFlipTableButton.setObjectName("salesFlipTableButton")
        self.horizontalLayout_4.addWidget(self.salesFlipTableButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.salesLoadTableButton = QtWidgets.QPushButton(self.tableFeatureFrame)
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
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/reload_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesLoadTableButton.setIcon(icon15)
        self.salesLoadTableButton.setIconSize(QtCore.QSize(20, 20))
        self.salesLoadTableButton.setObjectName("salesLoadTableButton")
        self.horizontalLayout_4.addWidget(self.salesLoadTableButton)
        self.salesPrevSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.salesPrevSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesPrevSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesPrevSearchButton.setFont(font)
        self.salesPrevSearchButton.setStyleSheet("QPushButton#salesPrevSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesPrevSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesPrevSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/undo_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesPrevSearchButton.setIcon(icon16)
        self.salesPrevSearchButton.setIconSize(QtCore.QSize(20, 20))
        self.salesPrevSearchButton.setObjectName("salesPrevSearchButton")
        self.horizontalLayout_4.addWidget(self.salesPrevSearchButton)
        self.salesNextSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame)
        self.salesNextSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.salesNextSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesNextSearchButton.setFont(font)
        self.salesNextSearchButton.setStyleSheet("QPushButton#salesNextSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#salesNextSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#salesNextSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("icons/redo_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salesNextSearchButton.setIcon(icon17)
        self.salesNextSearchButton.setIconSize(QtCore.QSize(20, 20))
        self.salesNextSearchButton.setObjectName("salesNextSearchButton")
        self.horizontalLayout_4.addWidget(self.salesNextSearchButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.tableFeatureFrame)
        self.salesRecordsTableWidget = QtWidgets.QTableWidget(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.salesRecordsTableWidget.setFont(font)
        self.salesRecordsTableWidget.setStyleSheet("QTableWidget {\n"
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
        self.salesRecordsTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.salesRecordsTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.salesRecordsTableWidget.setAlternatingRowColors(True)
        self.salesRecordsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.salesRecordsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.salesRecordsTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.salesRecordsTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.salesRecordsTableWidget.setShowGrid(False)
        self.salesRecordsTableWidget.setColumnCount(5)
        self.salesRecordsTableWidget.setObjectName("salesRecordsTableWidget")
        self.salesRecordsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesRecordsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesRecordsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesRecordsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesRecordsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.salesRecordsTableWidget.setHorizontalHeaderItem(4, item)
        self.salesRecordsTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.salesRecordsTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.salesRecordsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.salesRecordsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.salesRecordsTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.salesRecordsTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.salesRecordsTableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding-left: 5px;")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.salesCurrentDayTotalSalesLabel = QtWidgets.QLabel(self.widget_6)
        self.salesCurrentDayTotalSalesLabel.setMinimumSize(QtCore.QSize(200, 30))
        self.salesCurrentDayTotalSalesLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.salesCurrentDayTotalSalesLabel.setFont(font)
        self.salesCurrentDayTotalSalesLabel.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding-right: 5px;")
        self.salesCurrentDayTotalSalesLabel.setText("")
        self.salesCurrentDayTotalSalesLabel.setObjectName("salesCurrentDayTotalSalesLabel")
        self.horizontalLayout_2.addWidget(self.salesCurrentDayTotalSalesLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.contentStackedWidget.addWidget(self.salesPage)
        self.notificationPage = QtWidgets.QWidget()
        self.notificationPage.setObjectName("notificationPage")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.notificationPage)
        self.gridLayout_4.setContentsMargins(1, -1, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.notificationPage)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(99, 174, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QSplitter::handle:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(255, 255, 255, 255));;\n"
"}")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.gridWidget = QtWidgets.QWidget(self.splitter)
        self.gridWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.gridWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.gridWidget.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.gridWidget.setObjectName("gridWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gridWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.todayNotifButton = QtWidgets.QPushButton(self.gridWidget)
        self.todayNotifButton.setMinimumSize(QtCore.QSize(0, 50))
        self.todayNotifButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.todayNotifButton.setFont(font)
        self.todayNotifButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.todayNotifButton.setStyleSheet("QPushButton#todayNotifButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#todayNotifButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#todayNotifButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-left: 5px solid #ff8566;\n"
"}")
        self.todayNotifButton.setCheckable(True)
        self.todayNotifButton.setChecked(True)
        self.todayNotifButton.setObjectName("todayNotifButton")
        self.verticalLayout_6.addWidget(self.todayNotifButton)
        self.historyNotifButton = QtWidgets.QPushButton(self.gridWidget)
        self.historyNotifButton.setMinimumSize(QtCore.QSize(0, 50))
        self.historyNotifButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.historyNotifButton.setFont(font)
        self.historyNotifButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.historyNotifButton.setStyleSheet("QPushButton#historyNotifButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#historyNotifButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#historyNotifButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-left: 5px solid #ff8566;\n"
"}")
        self.historyNotifButton.setCheckable(True)
        self.historyNotifButton.setObjectName("historyNotifButton")
        self.verticalLayout_6.addWidget(self.historyNotifButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setMinimumSize(QtCore.QSize(250, 0))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.notifMsgLabel = QtWidgets.QLabel(self.widget)
        self.notifMsgLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.notifMsgLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.notifMsgLabel.setFont(font)
        self.notifMsgLabel.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;")
        self.notifMsgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notifMsgLabel.setObjectName("notifMsgLabel")
        self.horizontalLayout_10.addWidget(self.notifMsgLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.notifMsgListWidget = QtWidgets.QListWidget(self.widget)
        self.notifMsgListWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.notifMsgListWidget.setStyleSheet("QListWidget {\n"
"    border-top: 1px solid #63b946;\n"
"    padding: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-background-color: #ff8566;\n"
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
        self.notifMsgListWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notifMsgListWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.notifMsgListWidget.setAlternatingRowColors(False)
        self.notifMsgListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.notifMsgListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.notifMsgListWidget.setGridSize(QtCore.QSize(0, 85))
        self.notifMsgListWidget.setUniformItemSizes(True)
        self.notifMsgListWidget.setSelectionRectVisible(True)
        self.notifMsgListWidget.setObjectName("notifMsgListWidget")
        self.verticalLayout_8.addWidget(self.notifMsgListWidget)
        self.noNotifMsgLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.noNotifMsgLabel.setFont(font)
        self.noNotifMsgLabel.setStyleSheet("color: rgb(200, 200, 200);\n"
"border-top: 1px solid #63b946;")
        self.noNotifMsgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noNotifMsgLabel.setObjectName("noNotifMsgLabel")
        self.verticalLayout_8.addWidget(self.noNotifMsgLabel)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.viewNotifTextEdit = QtWidgets.QTextEdit(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.viewNotifTextEdit.setFont(font)
        self.viewNotifTextEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #ffffff;\n"
"    border-top: 1px solid #63b946;\n"
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
        self.viewNotifTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.viewNotifTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.viewNotifTextEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.viewNotifTextEdit.setReadOnly(True)
        self.viewNotifTextEdit.setPlaceholderText("")
        self.viewNotifTextEdit.setObjectName("viewNotifTextEdit")
        self.gridLayout_3.addWidget(self.viewNotifTextEdit, 1, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.notifMsgViewLabel = QtWidgets.QLabel(self.widget_2)
        self.notifMsgViewLabel.setMinimumSize(QtCore.QSize(120, 30))
        self.notifMsgViewLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.notifMsgViewLabel.setFont(font)
        self.notifMsgViewLabel.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;")
        self.notifMsgViewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notifMsgViewLabel.setObjectName("notifMsgViewLabel")
        self.horizontalLayout_12.addWidget(self.notifMsgViewLabel)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.contentStackedWidget.addWidget(self.notificationPage)
        self.recordsPage = QtWidgets.QWidget()
        self.recordsPage.setObjectName("recordsPage")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.recordsPage)
        self.gridLayout_7.setContentsMargins(1, 9, 1, 1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.recordsPage)
        self.splitter_2.setStyleSheet("QSplitter::handle {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(99, 174, 0, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"QSplitter::handle:pressed {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.splitter_2.setMidLineWidth(1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(5)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.graphicalViewsWidget = QtWidgets.QWidget(self.splitter_2)
        self.graphicalViewsWidget.setMinimumSize(QtCore.QSize(260, 0))
        self.graphicalViewsWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.graphicalViewsWidget.setStyleSheet("background-color: #ffffff")
        self.graphicalViewsWidget.setObjectName("graphicalViewsWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.graphicalViewsWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(289, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 2, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_3 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_3.setMinimumSize(QtCore.QSize(125, 30))
        self.label_3.setMaximumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffffff;\n"
"background-color: #63b946;\n"
"padding:5px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_15.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.label_2 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 1))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #63b946;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.frame_3 = QtWidgets.QFrame(self.graphicalViewsWidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("QFrame {\n"
"    background-color: rgb(230, 240, 230);\n"
"}\n"
"QMenu {\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    font-size: 14px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QMenu::item:pressed {\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.recordsDailyMonthComboBox = QtWidgets.QComboBox(self.frame_3)
        self.recordsDailyMonthComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsDailyMonthComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsDailyMonthComboBox.setFont(font)
        self.recordsDailyMonthComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.recordsDailyMonthComboBox.setObjectName("recordsDailyMonthComboBox")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.recordsDailyMonthComboBox.addItem("")
        self.horizontalLayout_16.addWidget(self.recordsDailyMonthComboBox)
        self.recordsDailyYearSpinBox = QtWidgets.QSpinBox(self.frame_3)
        self.recordsDailyYearSpinBox.setMinimumSize(QtCore.QSize(60, 30))
        self.recordsDailyYearSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsDailyYearSpinBox.setFont(font)
        self.recordsDailyYearSpinBox.setStyleSheet("background-color: #ffffff;")
        self.recordsDailyYearSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.recordsDailyYearSpinBox.setMinimum(1990)
        self.recordsDailyYearSpinBox.setMaximum(3000)
        self.recordsDailyYearSpinBox.setProperty("value", 2019)
        self.recordsDailyYearSpinBox.setObjectName("recordsDailyYearSpinBox")
        self.horizontalLayout_16.addWidget(self.recordsDailyYearSpinBox)
        self.dailyRecordsViewButton = QtWidgets.QToolButton(self.frame_3)
        self.dailyRecordsViewButton.setMinimumSize(QtCore.QSize(50, 30))
        self.dailyRecordsViewButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dailyRecordsViewButton.setFont(font)
        self.dailyRecordsViewButton.setStyleSheet("QToolButton#dailyRecordsViewButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QToolButton#dailyRecordsViewButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#dailyRecordsViewButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.dailyRecordsViewButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.dailyRecordsViewButton.setObjectName("dailyRecordsViewButton")
        self.horizontalLayout_16.addWidget(self.dailyRecordsViewButton)
        self.verticalLayout_9.addWidget(self.frame_3)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_4 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_4.setMinimumSize(QtCore.QSize(125, 30))
        self.label_4.setMaximumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ffffff;\n"
"background-color: #63b946;\n"
"padding:5px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_18.addWidget(self.label_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_18)
        self.label_5 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 1))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#63b946;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.frame_4 = QtWidgets.QFrame(self.graphicalViewsWidget)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: rgb(230, 240, 230);\n"
"}\n"
"QMenu {\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    font-size: 14px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QMenu::item:pressed {\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.recordsMonthlyYearSpinBox = QtWidgets.QSpinBox(self.frame_4)
        self.recordsMonthlyYearSpinBox.setMinimumSize(QtCore.QSize(60, 30))
        self.recordsMonthlyYearSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsMonthlyYearSpinBox.setFont(font)
        self.recordsMonthlyYearSpinBox.setStyleSheet("background-color: #ffffff;")
        self.recordsMonthlyYearSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.recordsMonthlyYearSpinBox.setMinimum(1990)
        self.recordsMonthlyYearSpinBox.setMaximum(3000)
        self.recordsMonthlyYearSpinBox.setProperty("value", 2019)
        self.recordsMonthlyYearSpinBox.setObjectName("recordsMonthlyYearSpinBox")
        self.horizontalLayout_19.addWidget(self.recordsMonthlyYearSpinBox)
        self.monthlyRecordsViewButton = QtWidgets.QToolButton(self.frame_4)
        self.monthlyRecordsViewButton.setMinimumSize(QtCore.QSize(50, 30))
        self.monthlyRecordsViewButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.monthlyRecordsViewButton.setFont(font)
        self.monthlyRecordsViewButton.setStyleSheet("QToolButton#monthlyRecordsViewButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QToolButton#monthlyRecordsViewButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#monthlyRecordsViewButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.monthlyRecordsViewButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.monthlyRecordsViewButton.setObjectName("monthlyRecordsViewButton")
        self.horizontalLayout_19.addWidget(self.monthlyRecordsViewButton)
        self.verticalLayout_9.addWidget(self.frame_4)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_6 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_6.setMinimumSize(QtCore.QSize(125, 30))
        self.label_6.setMaximumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ffffff;\n"
"background-color: #63b946;\n"
"padding:5px;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_20.addWidget(self.label_6)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.label_8 = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.label_8.setMinimumSize(QtCore.QSize(0, 1))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_8.setStyleSheet("background-color:#63b946;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.frame_5 = QtWidgets.QFrame(self.graphicalViewsWidget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("QFrame {\n"
"    background-color: rgb(230, 240, 230);\n"
"}\n"
"QMenu {\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    font-size: 14px;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QMenu::item:pressed {\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMinimumSize(QtCore.QSize(40, 30))
        self.label_11.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_21.addWidget(self.label_11)
        self.recordsYearlyFromYearSpinBox = QtWidgets.QSpinBox(self.frame_5)
        self.recordsYearlyFromYearSpinBox.setMinimumSize(QtCore.QSize(60, 30))
        self.recordsYearlyFromYearSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsYearlyFromYearSpinBox.setFont(font)
        self.recordsYearlyFromYearSpinBox.setStyleSheet("background-color:#ffffff;")
        self.recordsYearlyFromYearSpinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.recordsYearlyFromYearSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.recordsYearlyFromYearSpinBox.setMinimum(1990)
        self.recordsYearlyFromYearSpinBox.setMaximum(3000)
        self.recordsYearlyFromYearSpinBox.setProperty("value", 2019)
        self.recordsYearlyFromYearSpinBox.setObjectName("recordsYearlyFromYearSpinBox")
        self.horizontalLayout_21.addWidget(self.recordsYearlyFromYearSpinBox)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setMinimumSize(QtCore.QSize(20, 30))
        self.label_10.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_21.addWidget(self.label_10)
        self.recordsYearlyToYearSpinBox = QtWidgets.QSpinBox(self.frame_5)
        self.recordsYearlyToYearSpinBox.setMinimumSize(QtCore.QSize(60, 30))
        self.recordsYearlyToYearSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsYearlyToYearSpinBox.setFont(font)
        self.recordsYearlyToYearSpinBox.setStyleSheet("background-color:#ffffff;")
        self.recordsYearlyToYearSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.recordsYearlyToYearSpinBox.setMinimum(1990)
        self.recordsYearlyToYearSpinBox.setMaximum(3000)
        self.recordsYearlyToYearSpinBox.setProperty("value", 2019)
        self.recordsYearlyToYearSpinBox.setObjectName("recordsYearlyToYearSpinBox")
        self.horizontalLayout_21.addWidget(self.recordsYearlyToYearSpinBox)
        self.yearlyRecordsViewButton = QtWidgets.QToolButton(self.frame_5)
        self.yearlyRecordsViewButton.setMinimumSize(QtCore.QSize(50, 30))
        self.yearlyRecordsViewButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yearlyRecordsViewButton.setFont(font)
        self.yearlyRecordsViewButton.setStyleSheet("QToolButton#yearlyRecordsViewButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QToolButton#yearlyRecordsViewButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton#yearlyRecordsViewButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.yearlyRecordsViewButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.yearlyRecordsViewButton.setObjectName("yearlyRecordsViewButton")
        self.horizontalLayout_21.addWidget(self.yearlyRecordsViewButton)
        self.verticalLayout_9.addWidget(self.frame_5)
        self.gridLayout_6.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.loadingGraphAnimLabel = QtWidgets.QLabel(self.graphicalViewsWidget)
        self.loadingGraphAnimLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.loadingGraphAnimLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.loadingGraphAnimLabel.setText("")
        self.loadingGraphAnimLabel.setScaledContents(False)
        self.loadingGraphAnimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingGraphAnimLabel.setObjectName("loadingGraphAnimLabel")
        self.gridLayout_6.addWidget(self.loadingGraphAnimLabel, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.splitter_2)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_5.setContentsMargins(1, 0, 0, 0)
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableFeatureFrame_2 = QtWidgets.QFrame(self.widget_4)
        self.tableFeatureFrame_2.setMinimumSize(QtCore.QSize(0, 100))
        self.tableFeatureFrame_2.setStyleSheet("background-color:  rgb(230, 240, 230);")
        self.tableFeatureFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableFeatureFrame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableFeatureFrame_2.setObjectName("tableFeatureFrame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tableFeatureFrame_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.recordsSearchDateEdit = QtWidgets.QDateEdit(self.tableFeatureFrame_2)
        self.recordsSearchDateEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsSearchDateEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsSearchDateEdit.setFont(font)
        self.recordsSearchDateEdit.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.recordsSearchDateEdit.setFrame(False)
        self.recordsSearchDateEdit.setReadOnly(False)
        self.recordsSearchDateEdit.setTime(QtCore.QTime(0, 0, 0))
        self.recordsSearchDateEdit.setMaximumDate(QtCore.QDate(3000, 12, 31))
        self.recordsSearchDateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.recordsSearchDateEdit.setCalendarPopup(True)
        self.recordsSearchDateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.recordsSearchDateEdit.setObjectName("recordsSearchDateEdit")
        self.horizontalLayout_13.addWidget(self.recordsSearchDateEdit)
        self.recordsSearchParamComboBox = QtWidgets.QComboBox(self.tableFeatureFrame_2)
        self.recordsSearchParamComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsSearchParamComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsSearchParamComboBox.setFont(font)
        self.recordsSearchParamComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.recordsSearchParamComboBox.setMaxVisibleItems(3)
        self.recordsSearchParamComboBox.setFrame(True)
        self.recordsSearchParamComboBox.setObjectName("recordsSearchParamComboBox")
        self.recordsSearchParamComboBox.addItem("")
        self.recordsSearchParamComboBox.addItem("")
        self.recordsSearchParamComboBox.addItem("")
        self.recordsSearchParamComboBox.addItem("")
        self.horizontalLayout_13.addWidget(self.recordsSearchParamComboBox)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.recordsSearchField = QtWidgets.QLineEdit(self.tableFeatureFrame_2)
        self.recordsSearchField.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsSearchField.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsSearchField.setFont(font)
        self.recordsSearchField.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.recordsSearchField.setObjectName("recordsSearchField")
        self.horizontalLayout_14.addWidget(self.recordsSearchField)
        self.recordsSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame_2)
        self.recordsSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.recordsSearchButton.setFont(font)
        self.recordsSearchButton.setStyleSheet("QPushButton#recordsSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#recordsSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#recordsSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.recordsSearchButton.setIcon(icon13)
        self.recordsSearchButton.setIconSize(QtCore.QSize(25, 25))
        self.recordsSearchButton.setObjectName("recordsSearchButton")
        self.horizontalLayout_14.addWidget(self.recordsSearchButton)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.recordsSortLabel = QtWidgets.QLabel(self.tableFeatureFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordsSortLabel.sizePolicy().hasHeightForWidth())
        self.recordsSortLabel.setSizePolicy(sizePolicy)
        self.recordsSortLabel.setMinimumSize(QtCore.QSize(55, 30))
        self.recordsSortLabel.setMaximumSize(QtCore.QSize(55, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsSortLabel.setFont(font)
        self.recordsSortLabel.setObjectName("recordsSortLabel")
        self.horizontalLayout_22.addWidget(self.recordsSortLabel)
        self.recordsSortComboBox = QtWidgets.QComboBox(self.tableFeatureFrame_2)
        self.recordsSortComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.recordsSortComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsSortComboBox.setFont(font)
        self.recordsSortComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.recordsSortComboBox.setObjectName("recordsSortComboBox")
        self.recordsSortComboBox.addItem("")
        self.recordsSortComboBox.addItem("")
        self.horizontalLayout_22.addWidget(self.recordsSortComboBox)
        self.recordsFlipTableButton = QtWidgets.QPushButton(self.tableFeatureFrame_2)
        self.recordsFlipTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsFlipTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsFlipTableButton.setFont(font)
        self.recordsFlipTableButton.setStyleSheet("QPushButton#recordsFlipTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#recordsFlipTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#recordsFlipTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.recordsFlipTableButton.setIcon(icon14)
        self.recordsFlipTableButton.setIconSize(QtCore.QSize(20, 20))
        self.recordsFlipTableButton.setObjectName("recordsFlipTableButton")
        self.horizontalLayout_22.addWidget(self.recordsFlipTableButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem12)
        self.recordsLoadTableButton = QtWidgets.QPushButton(self.tableFeatureFrame_2)
        self.recordsLoadTableButton.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsLoadTableButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsLoadTableButton.setFont(font)
        self.recordsLoadTableButton.setStyleSheet("QPushButton#recordsLoadTableButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#recordsLoadTableButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#recordsLoadTableButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.recordsLoadTableButton.setIcon(icon15)
        self.recordsLoadTableButton.setIconSize(QtCore.QSize(20, 20))
        self.recordsLoadTableButton.setObjectName("recordsLoadTableButton")
        self.horizontalLayout_22.addWidget(self.recordsLoadTableButton)
        self.recordsPrevSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame_2)
        self.recordsPrevSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsPrevSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsPrevSearchButton.setFont(font)
        self.recordsPrevSearchButton.setStyleSheet("QPushButton#recordsPrevSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#recordsPrevSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#recordsPrevSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.recordsPrevSearchButton.setIcon(icon16)
        self.recordsPrevSearchButton.setIconSize(QtCore.QSize(20, 20))
        self.recordsPrevSearchButton.setObjectName("recordsPrevSearchButton")
        self.horizontalLayout_22.addWidget(self.recordsPrevSearchButton)
        self.recordsNextSearchButton = QtWidgets.QPushButton(self.tableFeatureFrame_2)
        self.recordsNextSearchButton.setMinimumSize(QtCore.QSize(0, 30))
        self.recordsNextSearchButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsNextSearchButton.setFont(font)
        self.recordsNextSearchButton.setStyleSheet("QPushButton#recordsNextSearchButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#recordsNextSearchButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#recordsNextSearchButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.recordsNextSearchButton.setIcon(icon17)
        self.recordsNextSearchButton.setIconSize(QtCore.QSize(20, 20))
        self.recordsNextSearchButton.setObjectName("recordsNextSearchButton")
        self.horizontalLayout_22.addWidget(self.recordsNextSearchButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_22)
        self.gridLayout_5.addWidget(self.tableFeatureFrame_2, 0, 0, 1, 1)
        self.recordsTableWidget = QtWidgets.QTableWidget(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.recordsTableWidget.setFont(font)
        self.recordsTableWidget.setStyleSheet("QTableWidget {\n"
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
        self.recordsTableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.recordsTableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.recordsTableWidget.setAlternatingRowColors(True)
        self.recordsTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.recordsTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.recordsTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.recordsTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.recordsTableWidget.setShowGrid(False)
        self.recordsTableWidget.setColumnCount(5)
        self.recordsTableWidget.setObjectName("recordsTableWidget")
        self.recordsTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordsTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordsTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordsTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordsTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recordsTableWidget.setHorizontalHeaderItem(4, item)
        self.recordsTableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.recordsTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.recordsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.recordsTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.recordsTableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_5.addWidget(self.recordsTableWidget, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setMinimumSize(QtCore.QSize(0, 30))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding-left: 5px;")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.historyCurrentDayTotalSalesLabel = QtWidgets.QLabel(self.widget_4)
        self.historyCurrentDayTotalSalesLabel.setMinimumSize(QtCore.QSize(200, 30))
        self.historyCurrentDayTotalSalesLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.historyCurrentDayTotalSalesLabel.setFont(font)
        self.historyCurrentDayTotalSalesLabel.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding-right: 5px;")
        self.historyCurrentDayTotalSalesLabel.setText("")
        self.historyCurrentDayTotalSalesLabel.setObjectName("historyCurrentDayTotalSalesLabel")
        self.horizontalLayout_6.addWidget(self.historyCurrentDayTotalSalesLabel)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.contentStackedWidget.addWidget(self.recordsPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsPage)
        self.gridLayout_2.setContentsMargins(1, -1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_4 = QtWidgets.QSplitter(self.settingsPage)
        self.splitter_4.setStyleSheet("QSplitter::handle {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(99, 174, 0, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"QSplitter::handle:pressed {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(37, 37, 37, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setHandleWidth(5)
        self.splitter_4.setChildrenCollapsible(False)
        self.splitter_4.setObjectName("splitter_4")
        self.widget_5 = QtWidgets.QWidget(self.splitter_4)
        self.widget_5.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(250, 16777215))
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.accountSettingsButton = QtWidgets.QPushButton(self.widget_5)
        self.accountSettingsButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.accountSettingsButton.setFont(font)
        self.accountSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.accountSettingsButton.setStyleSheet("QPushButton#accountSettingsButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#accountSettingsButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#accountSettingsButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-left: 5px solid #ff8566;\n"
"}")
        self.accountSettingsButton.setCheckable(True)
        self.accountSettingsButton.setChecked(True)
        self.accountSettingsButton.setObjectName("accountSettingsButton")
        self.verticalLayout_5.addWidget(self.accountSettingsButton)
        self.stockSettingsButton = QtWidgets.QPushButton(self.widget_5)
        self.stockSettingsButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.stockSettingsButton.setFont(font)
        self.stockSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stockSettingsButton.setAutoFillBackground(False)
        self.stockSettingsButton.setStyleSheet("QPushButton#stockSettingsButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#stockSettingsButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#stockSettingsButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-left: 5px solid #ff8566;\n"
"}")
        self.stockSettingsButton.setCheckable(True)
        self.stockSettingsButton.setObjectName("stockSettingsButton")
        self.verticalLayout_5.addWidget(self.stockSettingsButton)
        self.otherSettingsButton = QtWidgets.QPushButton(self.widget_5)
        self.otherSettingsButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.otherSettingsButton.setFont(font)
        self.otherSettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.otherSettingsButton.setStyleSheet("QPushButton#otherSettingsButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton#otherSettingsButton:hover{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton#otherSettingsButton:checked{\n"
"    color: #63b946;\n"
"    background-color: #ffffff;\n"
"    border-left: 5px solid #ff8566;\n"
"}")
        self.otherSettingsButton.setCheckable(True)
        self.otherSettingsButton.setObjectName("otherSettingsButton")
        self.verticalLayout_5.addWidget(self.otherSettingsButton)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem14)
        self.settingsStackedWidget = QtWidgets.QStackedWidget(self.splitter_4)
        self.settingsStackedWidget.setStyleSheet("QPushButton#addNewItemConfirmButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#addNewItemConfirmButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addNewItemConfirmButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.settingsStackedWidget.setObjectName("settingsStackedWidget")
        self.accountSettingsPage = QtWidgets.QWidget()
        self.accountSettingsPage.setObjectName("accountSettingsPage")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.accountSettingsPage)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setHorizontalSpacing(5)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_6 = QtWidgets.QFrame(self.accountSettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setMinimumSize(QtCore.QSize(185, 30))
        self.label_17.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_29.addWidget(self.label_17)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem15)
        self.verticalLayout_16.addLayout(self.horizontalLayout_29)
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_24.setStyleSheet("background-color:#63b946;")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_16.addWidget(self.label_24)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_25 = QtWidgets.QLabel(self.frame_9)
        self.label_25.setMinimumSize(QtCore.QSize(140, 30))
        self.label_25.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.editSalesPersonUsernameComboBox = QtWidgets.QComboBox(self.frame_9)
        self.editSalesPersonUsernameComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.editSalesPersonUsernameComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editSalesPersonUsernameComboBox.setFont(font)
        self.editSalesPersonUsernameComboBox.setStyleSheet("color: #000000;\n"
"background-color: #ffffff;")
        self.editSalesPersonUsernameComboBox.setEditable(False)
        self.editSalesPersonUsernameComboBox.setDuplicatesEnabled(True)
        self.editSalesPersonUsernameComboBox.setFrame(False)
        self.editSalesPersonUsernameComboBox.setObjectName("editSalesPersonUsernameComboBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editSalesPersonUsernameComboBox)
        self.label_26 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(140, 30))
        self.label_26.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.editSalesPersonNewUsernameLineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.editSalesPersonNewUsernameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editSalesPersonNewUsernameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editSalesPersonNewUsernameLineEdit.setFont(font)
        self.editSalesPersonNewUsernameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editSalesPersonNewUsernameLineEdit.setObjectName("editSalesPersonNewUsernameLineEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editSalesPersonNewUsernameLineEdit)
        self.label_27 = QtWidgets.QLabel(self.frame_9)
        self.label_27.setMinimumSize(QtCore.QSize(140, 30))
        self.label_27.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.editSalesPersonNewPasswordLineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.editSalesPersonNewPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editSalesPersonNewPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editSalesPersonNewPasswordLineEdit.setFont(font)
        self.editSalesPersonNewPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editSalesPersonNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSalesPersonNewPasswordLineEdit.setObjectName("editSalesPersonNewPasswordLineEdit")
        self.horizontalLayout_47.addWidget(self.editSalesPersonNewPasswordLineEdit)
        self.editSalesPersonShowHideNewPasswordButton = QtWidgets.QPushButton(self.frame_9)
        self.editSalesPersonShowHideNewPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editSalesPersonShowHideNewPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.editSalesPersonShowHideNewPasswordButton.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("icons/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editSalesPersonShowHideNewPasswordButton.setIcon(icon18)
        self.editSalesPersonShowHideNewPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editSalesPersonShowHideNewPasswordButton.setFlat(True)
        self.editSalesPersonShowHideNewPasswordButton.setObjectName("editSalesPersonShowHideNewPasswordButton")
        self.horizontalLayout_47.addWidget(self.editSalesPersonShowHideNewPasswordButton)
        self.formLayout_4.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_47)
        self.label_28 = QtWidgets.QLabel(self.frame_9)
        self.label_28.setMinimumSize(QtCore.QSize(140, 30))
        self.label_28.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.editSalesPersonConfirmNewPasswordLineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.editSalesPersonConfirmNewPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editSalesPersonConfirmNewPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editSalesPersonConfirmNewPasswordLineEdit.setFont(font)
        self.editSalesPersonConfirmNewPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.editSalesPersonConfirmNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSalesPersonConfirmNewPasswordLineEdit.setObjectName("editSalesPersonConfirmNewPasswordLineEdit")
        self.horizontalLayout_44.addWidget(self.editSalesPersonConfirmNewPasswordLineEdit)
        self.editSalesPersonShowHideConfirmPasswordButton = QtWidgets.QPushButton(self.frame_9)
        self.editSalesPersonShowHideConfirmPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editSalesPersonShowHideConfirmPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.editSalesPersonShowHideConfirmPasswordButton.setText("")
        self.editSalesPersonShowHideConfirmPasswordButton.setIcon(icon18)
        self.editSalesPersonShowHideConfirmPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editSalesPersonShowHideConfirmPasswordButton.setFlat(True)
        self.editSalesPersonShowHideConfirmPasswordButton.setObjectName("editSalesPersonShowHideConfirmPasswordButton")
        self.horizontalLayout_44.addWidget(self.editSalesPersonShowHideConfirmPasswordButton)
        self.formLayout_4.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_44)
        self.label_31 = QtWidgets.QLabel(self.frame_9)
        self.label_31.setMinimumSize(QtCore.QSize(140, 30))
        self.label_31.setMaximumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_32.setSpacing(10)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_32.addItem(spacerItem16)
        self.editSalesPerosnCancelButton = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editSalesPerosnCancelButton.sizePolicy().hasHeightForWidth())
        self.editSalesPerosnCancelButton.setSizePolicy(sizePolicy)
        self.editSalesPerosnCancelButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editSalesPerosnCancelButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.editSalesPerosnCancelButton.setFont(font)
        self.editSalesPerosnCancelButton.setStyleSheet("QPushButton#editSalesPerosnCancelButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editSalesPerosnCancelButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editSalesPerosnCancelButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editSalesPerosnCancelButton.setObjectName("editSalesPerosnCancelButton")
        self.horizontalLayout_32.addWidget(self.editSalesPerosnCancelButton)
        self.editSalesPersonSaveButton = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editSalesPersonSaveButton.sizePolicy().hasHeightForWidth())
        self.editSalesPersonSaveButton.setSizePolicy(sizePolicy)
        self.editSalesPersonSaveButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editSalesPersonSaveButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.editSalesPersonSaveButton.setFont(font)
        self.editSalesPersonSaveButton.setStyleSheet("QPushButton#editSalesPersonSaveButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editSalesPersonSaveButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editSalesPersonSaveButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editSalesPersonSaveButton.setObjectName("editSalesPersonSaveButton")
        self.horizontalLayout_32.addWidget(self.editSalesPersonSaveButton)
        self.formLayout_4.setLayout(6, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_32)
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.editSalesPersonCurrentPasswordLineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.editSalesPersonCurrentPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editSalesPersonCurrentPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editSalesPersonCurrentPasswordLineEdit.setFont(font)
        self.editSalesPersonCurrentPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editSalesPersonCurrentPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editSalesPersonCurrentPasswordLineEdit.setObjectName("editSalesPersonCurrentPasswordLineEdit")
        self.horizontalLayout_50.addWidget(self.editSalesPersonCurrentPasswordLineEdit)
        self.editSalesPersonShowHideCurrentPasswordButton = QtWidgets.QPushButton(self.frame_9)
        self.editSalesPersonShowHideCurrentPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editSalesPersonShowHideCurrentPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.editSalesPersonShowHideCurrentPasswordButton.setFont(font)
        self.editSalesPersonShowHideCurrentPasswordButton.setText("")
        self.editSalesPersonShowHideCurrentPasswordButton.setIcon(icon18)
        self.editSalesPersonShowHideCurrentPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editSalesPersonShowHideCurrentPasswordButton.setFlat(True)
        self.editSalesPersonShowHideCurrentPasswordButton.setObjectName("editSalesPersonShowHideCurrentPasswordButton")
        self.horizontalLayout_50.addWidget(self.editSalesPersonShowHideCurrentPasswordButton)
        self.formLayout_4.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_50)
        self.gridLayout_11.addLayout(self.formLayout_4, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem17, 2, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem18, 1, 0, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem19, 1, 2, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_11.addItem(spacerItem20, 0, 1, 1, 1)
        self.verticalLayout_16.addWidget(self.frame_9)
        self.gridLayout_12.addWidget(self.frame_6, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.accountSettingsPage)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(185, 30))
        self.label.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_9.addWidget(self.label)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem21)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_15.setStyleSheet("background-color: #63b946;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_13.addWidget(self.label_15)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("background-color:rgb(230, 240, 230);r")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem22, 2, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem23, 1, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_10.addItem(spacerItem24, 0, 1, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem25, 1, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setMinimumSize(QtCore.QSize(130, 30))
        self.label_18.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.addSalesPersonUsernameLineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.addSalesPersonUsernameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.addSalesPersonUsernameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addSalesPersonUsernameLineEdit.setFont(font)
        self.addSalesPersonUsernameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.addSalesPersonUsernameLineEdit.setObjectName("addSalesPersonUsernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.addSalesPersonUsernameLineEdit)
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setMinimumSize(QtCore.QSize(130, 30))
        self.label_19.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setMinimumSize(QtCore.QSize(130, 30))
        self.label_20.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem26)
        self.addSalesPersonClearButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSalesPersonClearButton.sizePolicy().hasHeightForWidth())
        self.addSalesPersonClearButton.setSizePolicy(sizePolicy)
        self.addSalesPersonClearButton.setMinimumSize(QtCore.QSize(100, 30))
        self.addSalesPersonClearButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.addSalesPersonClearButton.setFont(font)
        self.addSalesPersonClearButton.setStyleSheet("QPushButton#addSalesPersonClearButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#addSalesPersonClearButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addSalesPersonClearButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.addSalesPersonClearButton.setObjectName("addSalesPersonClearButton")
        self.horizontalLayout_27.addWidget(self.addSalesPersonClearButton)
        self.addSalesPersonSubmitButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSalesPersonSubmitButton.sizePolicy().hasHeightForWidth())
        self.addSalesPersonSubmitButton.setSizePolicy(sizePolicy)
        self.addSalesPersonSubmitButton.setMinimumSize(QtCore.QSize(100, 30))
        self.addSalesPersonSubmitButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.addSalesPersonSubmitButton.setFont(font)
        self.addSalesPersonSubmitButton.setStyleSheet("QPushButton#addSalesPersonSubmitButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#addSalesPersonSubmitButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addSalesPersonSubmitButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.addSalesPersonSubmitButton.setObjectName("addSalesPersonSubmitButton")
        self.horizontalLayout_27.addWidget(self.addSalesPersonSubmitButton)
        self.viewAllSalesPersonsButton = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewAllSalesPersonsButton.sizePolicy().hasHeightForWidth())
        self.viewAllSalesPersonsButton.setSizePolicy(sizePolicy)
        self.viewAllSalesPersonsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.viewAllSalesPersonsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.viewAllSalesPersonsButton.setFont(font)
        self.viewAllSalesPersonsButton.setStyleSheet("QPushButton#viewAllSalesPersonsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#viewAllSalesPersonsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#viewAllSalesPersonsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.viewAllSalesPersonsButton.setObjectName("viewAllSalesPersonsButton")
        self.horizontalLayout_27.addWidget(self.viewAllSalesPersonsButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_27)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.addSalesPersonConfirmPasswordLineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.addSalesPersonConfirmPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.addSalesPersonConfirmPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addSalesPersonConfirmPasswordLineEdit.setFont(font)
        self.addSalesPersonConfirmPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.addSalesPersonConfirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.addSalesPersonConfirmPasswordLineEdit.setObjectName("addSalesPersonConfirmPasswordLineEdit")
        self.gridLayout_8.addWidget(self.addSalesPersonConfirmPasswordLineEdit, 0, 0, 1, 1)
        self.addSalesPersonShowHideConfirmPasswordButton = QtWidgets.QPushButton(self.frame_7)
        self.addSalesPersonShowHideConfirmPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.addSalesPersonShowHideConfirmPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.addSalesPersonShowHideConfirmPasswordButton.setText("")
        self.addSalesPersonShowHideConfirmPasswordButton.setIcon(icon18)
        self.addSalesPersonShowHideConfirmPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.addSalesPersonShowHideConfirmPasswordButton.setFlat(True)
        self.addSalesPersonShowHideConfirmPasswordButton.setObjectName("addSalesPersonShowHideConfirmPasswordButton")
        self.gridLayout_8.addWidget(self.addSalesPersonShowHideConfirmPasswordButton, 0, 1, 1, 1)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.gridLayout_8)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.addSalesPersonPasswordLineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.addSalesPersonPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.addSalesPersonPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addSalesPersonPasswordLineEdit.setFont(font)
        self.addSalesPersonPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.addSalesPersonPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.addSalesPersonPasswordLineEdit.setObjectName("addSalesPersonPasswordLineEdit")
        self.horizontalLayout_33.addWidget(self.addSalesPersonPasswordLineEdit)
        self.addSalesPersonHideShowPasswordButton = QtWidgets.QPushButton(self.frame_7)
        self.addSalesPersonHideShowPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.addSalesPersonHideShowPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.addSalesPersonHideShowPasswordButton.setText("")
        self.addSalesPersonHideShowPasswordButton.setIcon(icon18)
        self.addSalesPersonHideShowPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.addSalesPersonHideShowPasswordButton.setFlat(True)
        self.addSalesPersonHideShowPasswordButton.setObjectName("addSalesPersonHideShowPasswordButton")
        self.horizontalLayout_33.addWidget(self.addSalesPersonHideShowPasswordButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_33)
        self.gridLayout_10.addLayout(self.formLayout, 1, 1, 1, 1)
        self.verticalLayout_13.addWidget(self.frame_7)
        self.gridLayout_12.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.accountSettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setMinimumSize(QtCore.QSize(185, 30))
        self.label_14.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_25.addWidget(self.label_14)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem27)
        self.verticalLayout_14.addLayout(self.horizontalLayout_25)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_16.setStyleSheet("background-color: #63b946;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_14.addWidget(self.label_16)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_21 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(130, 30))
        self.label_21.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.removeSalesPersonUsernameComboBox = QtWidgets.QComboBox(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeSalesPersonUsernameComboBox.sizePolicy().hasHeightForWidth())
        self.removeSalesPersonUsernameComboBox.setSizePolicy(sizePolicy)
        self.removeSalesPersonUsernameComboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.removeSalesPersonUsernameComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeSalesPersonUsernameComboBox.setFont(font)
        self.removeSalesPersonUsernameComboBox.setStyleSheet("color: #000000;\n"
"background-color:#ffffff;")
        self.removeSalesPersonUsernameComboBox.setEditable(False)
        self.removeSalesPersonUsernameComboBox.setDuplicatesEnabled(True)
        self.removeSalesPersonUsernameComboBox.setFrame(False)
        self.removeSalesPersonUsernameComboBox.setObjectName("removeSalesPersonUsernameComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.removeSalesPersonUsernameComboBox)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem28)
        self.removeSalesPersonRevokeButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeSalesPersonRevokeButton.sizePolicy().hasHeightForWidth())
        self.removeSalesPersonRevokeButton.setSizePolicy(sizePolicy)
        self.removeSalesPersonRevokeButton.setMinimumSize(QtCore.QSize(100, 30))
        self.removeSalesPersonRevokeButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.removeSalesPersonRevokeButton.setFont(font)
        self.removeSalesPersonRevokeButton.setStyleSheet("QPushButton#removeSalesPersonRevokeButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#removeSalesPersonRevokeButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#removeSalesPersonRevokeButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.removeSalesPersonRevokeButton.setObjectName("removeSalesPersonRevokeButton")
        self.horizontalLayout_28.addWidget(self.removeSalesPersonRevokeButton)
        self.removeSalesPersonConfirmButton = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeSalesPersonConfirmButton.sizePolicy().hasHeightForWidth())
        self.removeSalesPersonConfirmButton.setSizePolicy(sizePolicy)
        self.removeSalesPersonConfirmButton.setMinimumSize(QtCore.QSize(100, 30))
        self.removeSalesPersonConfirmButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.removeSalesPersonConfirmButton.setFont(font)
        self.removeSalesPersonConfirmButton.setStyleSheet("QPushButton#removeSalesPersonConfirmButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#removeSalesPersonConfirmButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#removeSalesPersonConfirmButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.removeSalesPersonConfirmButton.setObjectName("removeSalesPersonConfirmButton")
        self.horizontalLayout_28.addWidget(self.removeSalesPersonConfirmButton)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_28)
        self.gridLayout_9.addLayout(self.formLayout_2, 1, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem29, 1, 2, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem30, 1, 0, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_9.addItem(spacerItem31, 0, 1, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem32, 2, 1, 1, 1)
        self.verticalLayout_14.addWidget(self.frame_8)
        self.gridLayout_12.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.accountSettingsPage)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_22 = QtWidgets.QLabel(self.frame_11)
        self.label_22.setMinimumSize(QtCore.QSize(185, 30))
        self.label_22.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_31.addWidget(self.label_22)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem33)
        self.gridLayout_13.addLayout(self.horizontalLayout_31, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_11)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_23.setStyleSheet("background-color: #63b946;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 1, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem34, 1, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setContentsMargins(0, 0, 0, -1)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_29 = QtWidgets.QLabel(self.frame_12)
        self.label_29.setMinimumSize(QtCore.QSize(130, 30))
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_29.setSizeIncrement(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.editAdminNameLineEdit = QtWidgets.QLineEdit(self.frame_12)
        self.editAdminNameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editAdminNameLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editAdminNameLineEdit.setFont(font)
        self.editAdminNameLineEdit.setStyleSheet("border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editAdminNameLineEdit.setReadOnly(True)
        self.editAdminNameLineEdit.setObjectName("editAdminNameLineEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editAdminNameLineEdit)
        self.label_30 = QtWidgets.QLabel(self.frame_12)
        self.label_30.setMinimumSize(QtCore.QSize(130, 30))
        self.label_30.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.label_32 = QtWidgets.QLabel(self.frame_12)
        self.label_32.setMinimumSize(QtCore.QSize(130, 30))
        self.label_32.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.label_33 = QtWidgets.QLabel(self.frame_12)
        self.label_33.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem35)
        self.editAdminCancelButton = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editAdminCancelButton.sizePolicy().hasHeightForWidth())
        self.editAdminCancelButton.setSizePolicy(sizePolicy)
        self.editAdminCancelButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editAdminCancelButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.editAdminCancelButton.setFont(font)
        self.editAdminCancelButton.setStyleSheet("QPushButton#editAdminCancelButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editAdminCancelButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editAdminCancelButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editAdminCancelButton.setObjectName("editAdminCancelButton")
        self.horizontalLayout_26.addWidget(self.editAdminCancelButton)
        self.editAdminSaveButton = QtWidgets.QPushButton(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editAdminSaveButton.sizePolicy().hasHeightForWidth())
        self.editAdminSaveButton.setSizePolicy(sizePolicy)
        self.editAdminSaveButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editAdminSaveButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.editAdminSaveButton.setFont(font)
        self.editAdminSaveButton.setStyleSheet("QPushButton#editAdminSaveButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editAdminSaveButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editAdminSaveButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editAdminSaveButton.setObjectName("editAdminSaveButton")
        self.horizontalLayout_26.addWidget(self.editAdminSaveButton)
        self.formLayout_5.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_26)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.editAdminConfirmPasswordLineEdit = QtWidgets.QLineEdit(self.frame_12)
        self.editAdminConfirmPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editAdminConfirmPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editAdminConfirmPasswordLineEdit.setFont(font)
        self.editAdminConfirmPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.editAdminConfirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editAdminConfirmPasswordLineEdit.setObjectName("editAdminConfirmPasswordLineEdit")
        self.horizontalLayout_51.addWidget(self.editAdminConfirmPasswordLineEdit)
        self.editAdminShowHideConfirmPasswordButton = QtWidgets.QPushButton(self.frame_12)
        self.editAdminShowHideConfirmPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideConfirmPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideConfirmPasswordButton.setText("")
        self.editAdminShowHideConfirmPasswordButton.setIcon(icon18)
        self.editAdminShowHideConfirmPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editAdminShowHideConfirmPasswordButton.setFlat(True)
        self.editAdminShowHideConfirmPasswordButton.setObjectName("editAdminShowHideConfirmPasswordButton")
        self.horizontalLayout_51.addWidget(self.editAdminShowHideConfirmPasswordButton)
        self.formLayout_5.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_51)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.editAdminNewPasswordLineEdit = QtWidgets.QLineEdit(self.frame_12)
        self.editAdminNewPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editAdminNewPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editAdminNewPasswordLineEdit.setFont(font)
        self.editAdminNewPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editAdminNewPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editAdminNewPasswordLineEdit.setObjectName("editAdminNewPasswordLineEdit")
        self.horizontalLayout_52.addWidget(self.editAdminNewPasswordLineEdit)
        self.editAdminShowHideNewPasswordButton = QtWidgets.QPushButton(self.frame_12)
        self.editAdminShowHideNewPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideNewPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideNewPasswordButton.setText("")
        self.editAdminShowHideNewPasswordButton.setIcon(icon18)
        self.editAdminShowHideNewPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editAdminShowHideNewPasswordButton.setFlat(True)
        self.editAdminShowHideNewPasswordButton.setObjectName("editAdminShowHideNewPasswordButton")
        self.horizontalLayout_52.addWidget(self.editAdminShowHideNewPasswordButton)
        self.formLayout_5.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_52)
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.editAdminCurrentPasswordLineEdit = QtWidgets.QLineEdit(self.frame_12)
        self.editAdminCurrentPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editAdminCurrentPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editAdminCurrentPasswordLineEdit.setFont(font)
        self.editAdminCurrentPasswordLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;")
        self.editAdminCurrentPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editAdminCurrentPasswordLineEdit.setObjectName("editAdminCurrentPasswordLineEdit")
        self.horizontalLayout_53.addWidget(self.editAdminCurrentPasswordLineEdit)
        self.editAdminShowHideCurrentPasswordButton = QtWidgets.QPushButton(self.frame_12)
        self.editAdminShowHideCurrentPasswordButton.setMinimumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideCurrentPasswordButton.setMaximumSize(QtCore.QSize(30, 30))
        self.editAdminShowHideCurrentPasswordButton.setText("")
        self.editAdminShowHideCurrentPasswordButton.setIcon(icon18)
        self.editAdminShowHideCurrentPasswordButton.setIconSize(QtCore.QSize(20, 20))
        self.editAdminShowHideCurrentPasswordButton.setFlat(True)
        self.editAdminShowHideCurrentPasswordButton.setObjectName("editAdminShowHideCurrentPasswordButton")
        self.horizontalLayout_53.addWidget(self.editAdminShowHideCurrentPasswordButton)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_53)
        self.gridLayout_14.addLayout(self.formLayout_5, 1, 1, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem36, 1, 2, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem37, 2, 1, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_14.addItem(spacerItem38, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frame_12, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_11, 1, 1, 1, 1)
        self.settingsStackedWidget.addWidget(self.accountSettingsPage)
        self.stockSettingsPage = QtWidgets.QWidget()
        self.stockSettingsPage.setObjectName("stockSettingsPage")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.stockSettingsPage)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setHorizontalSpacing(5)
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_14 = QtWidgets.QFrame(self.stockSettingsPage)
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setStyleSheet("background-color:rgb(230, 240, 230)")
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem39 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem39, 1, 2, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setContentsMargins(0, 0, 0, -1)
        self.formLayout_6.setVerticalSpacing(10)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_40 = QtWidgets.QLabel(self.frame_17)
        self.label_40.setMinimumSize(QtCore.QSize(110, 30))
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.addNewItemDescLineEdit = QtWidgets.QLineEdit(self.frame_17)
        self.addNewItemDescLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.addNewItemDescLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addNewItemDescLineEdit.setFont(font)
        self.addNewItemDescLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.addNewItemDescLineEdit.setObjectName("addNewItemDescLineEdit")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.addNewItemDescLineEdit)
        self.label_41 = QtWidgets.QLabel(self.frame_17)
        self.label_41.setMinimumSize(QtCore.QSize(110, 30))
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_51 = QtWidgets.QLabel(self.frame_17)
        self.label_51.setMinimumSize(QtCore.QSize(40, 30))
        self.label_51.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("background-color:#ffffff;")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_40.addWidget(self.label_51)
        self.addNewItemUnitPriceSpinBox = QtWidgets.QDoubleSpinBox(self.frame_17)
        self.addNewItemUnitPriceSpinBox.setMinimumSize(QtCore.QSize(135, 30))
        self.addNewItemUnitPriceSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addNewItemUnitPriceSpinBox.setFont(font)
        self.addNewItemUnitPriceSpinBox.setStyleSheet("background-color:#ffffff;")
        self.addNewItemUnitPriceSpinBox.setFrame(False)
        self.addNewItemUnitPriceSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.addNewItemUnitPriceSpinBox.setMaximum(1e+16)
        self.addNewItemUnitPriceSpinBox.setObjectName("addNewItemUnitPriceSpinBox")
        self.horizontalLayout_40.addWidget(self.addNewItemUnitPriceSpinBox)
        self.formLayout_6.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_40)
        self.label_42 = QtWidgets.QLabel(self.frame_17)
        self.label_42.setMinimumSize(QtCore.QSize(110, 30))
        self.label_42.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.addNewItemQtySpinBox = QtWidgets.QSpinBox(self.frame_17)
        self.addNewItemQtySpinBox.setMinimumSize(QtCore.QSize(135, 30))
        self.addNewItemQtySpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addNewItemQtySpinBox.setFont(font)
        self.addNewItemQtySpinBox.setStyleSheet("background-color:#ffffff;")
        self.addNewItemQtySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.addNewItemQtySpinBox.setMinimum(1)
        self.addNewItemQtySpinBox.setMaximum(2145778999)
        self.addNewItemQtySpinBox.setObjectName("addNewItemQtySpinBox")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.addNewItemQtySpinBox)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_37.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_37.setSpacing(10)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem40)
        self.addNewItemClearButton = QtWidgets.QPushButton(self.frame_17)
        self.addNewItemClearButton.setMinimumSize(QtCore.QSize(100, 30))
        self.addNewItemClearButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.addNewItemClearButton.setFont(font)
        self.addNewItemClearButton.setStyleSheet("QPushButton#addNewItemClearButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#addNewItemClearButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addNewItemClearButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.addNewItemClearButton.setObjectName("addNewItemClearButton")
        self.horizontalLayout_37.addWidget(self.addNewItemClearButton)
        self.addNewItemAddButton = QtWidgets.QPushButton(self.frame_17)
        self.addNewItemAddButton.setMinimumSize(QtCore.QSize(100, 30))
        self.addNewItemAddButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.addNewItemAddButton.setFont(font)
        self.addNewItemAddButton.setStyleSheet("QPushButton#addNewItemAddButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#addNewItemAddButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#addNewItemAddButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.addNewItemAddButton.setObjectName("addNewItemAddButton")
        self.horizontalLayout_37.addWidget(self.addNewItemAddButton)
        self.viewAllItemsButton = QtWidgets.QPushButton(self.frame_17)
        self.viewAllItemsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.viewAllItemsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.viewAllItemsButton.setFont(font)
        self.viewAllItemsButton.setStyleSheet("QPushButton#viewAllItemsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#viewAllItemsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#viewAllItemsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.viewAllItemsButton.setObjectName("viewAllItemsButton")
        self.horizontalLayout_37.addWidget(self.viewAllItemsButton)
        self.formLayout_6.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_37)
        self.gridLayout_20.addLayout(self.formLayout_6, 1, 1, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem41, 2, 1, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem42, 1, 0, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_20.addItem(spacerItem43, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.frame_17, 2, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.frame_15)
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_39.setStyleSheet("background-color: #63b946;")
        self.label_39.setText("")
        self.label_39.setObjectName("label_39")
        self.gridLayout_17.addWidget(self.label_39, 1, 0, 1, 1)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_38 = QtWidgets.QLabel(self.frame_15)
        self.label_38.setMinimumSize(QtCore.QSize(185, 30))
        self.label_38.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_34.addWidget(self.label_38)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem44)
        self.gridLayout_17.addLayout(self.horizontalLayout_34, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame_15, 0, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setStyleSheet("background-color:rgb(230, 240, 230)")
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setContentsMargins(0, 0, 0, -1)
        self.formLayout_7.setVerticalSpacing(10)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_43 = QtWidgets.QLabel(self.frame_18)
        self.label_43.setMinimumSize(QtCore.QSize(120, 30))
        self.label_43.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.removeItemChooseItemComboBox = QtWidgets.QComboBox(self.frame_18)
        self.removeItemChooseItemComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.removeItemChooseItemComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeItemChooseItemComboBox.setFont(font)
        self.removeItemChooseItemComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.removeItemChooseItemComboBox.setEditable(True)
        self.removeItemChooseItemComboBox.setDuplicatesEnabled(True)
        self.removeItemChooseItemComboBox.setFrame(False)
        self.removeItemChooseItemComboBox.setObjectName("removeItemChooseItemComboBox")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.removeItemChooseItemComboBox)
        self.label_34 = QtWidgets.QLabel(self.frame_18)
        self.label_34.setMinimumSize(QtCore.QSize(120, 30))
        self.label_34.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_50 = QtWidgets.QLabel(self.frame_18)
        self.label_50.setMinimumSize(QtCore.QSize(40, 0))
        self.label_50.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_39.addWidget(self.label_50)
        self.removeItemUnitPriceLineEdit = QtWidgets.QLineEdit(self.frame_18)
        self.removeItemUnitPriceLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.removeItemUnitPriceLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeItemUnitPriceLineEdit.setFont(font)
        self.removeItemUnitPriceLineEdit.setStyleSheet("border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.removeItemUnitPriceLineEdit.setReadOnly(True)
        self.removeItemUnitPriceLineEdit.setObjectName("removeItemUnitPriceLineEdit")
        self.horizontalLayout_39.addWidget(self.removeItemUnitPriceLineEdit)
        self.formLayout_7.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_39)
        self.label_44 = QtWidgets.QLabel(self.frame_18)
        self.label_44.setMinimumSize(QtCore.QSize(120, 30))
        self.label_44.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.removeItemQtyLineEdit = QtWidgets.QLineEdit(self.frame_18)
        self.removeItemQtyLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.removeItemQtyLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeItemQtyLineEdit.setFont(font)
        self.removeItemQtyLineEdit.setStyleSheet("border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.removeItemQtyLineEdit.setReadOnly(True)
        self.removeItemQtyLineEdit.setObjectName("removeItemQtyLineEdit")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.removeItemQtyLineEdit)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_38.setSpacing(10)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem45)
        self.removeItemClearButton = QtWidgets.QPushButton(self.frame_18)
        self.removeItemClearButton.setMinimumSize(QtCore.QSize(100, 30))
        self.removeItemClearButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeItemClearButton.setFont(font)
        self.removeItemClearButton.setStyleSheet("QPushButton#removeItemClearButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#removeItemClearButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#removeItemClearButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.removeItemClearButton.setObjectName("removeItemClearButton")
        self.horizontalLayout_38.addWidget(self.removeItemClearButton)
        self.removeItemRemoveButton = QtWidgets.QPushButton(self.frame_18)
        self.removeItemRemoveButton.setMinimumSize(QtCore.QSize(100, 30))
        self.removeItemRemoveButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.removeItemRemoveButton.setFont(font)
        self.removeItemRemoveButton.setStyleSheet("QPushButton#removeItemRemoveButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#removeItemRemoveButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#removeItemRemoveButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.removeItemRemoveButton.setObjectName("removeItemRemoveButton")
        self.horizontalLayout_38.addWidget(self.removeItemRemoveButton)
        self.formLayout_7.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_38)
        self.gridLayout_21.addLayout(self.formLayout_7, 1, 1, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem46, 1, 0, 1, 1)
        spacerItem47 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_21.addItem(spacerItem47, 0, 1, 1, 1)
        spacerItem48 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem48, 1, 2, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem49, 2, 1, 1, 1)
        self.gridLayout_18.addWidget(self.frame_18, 2, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.frame_16)
        self.label_37.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_37.setStyleSheet("background-color: #63b946;")
        self.label_37.setText("")
        self.label_37.setObjectName("label_37")
        self.gridLayout_18.addWidget(self.label_37, 1, 0, 1, 1)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_36 = QtWidgets.QLabel(self.frame_16)
        self.label_36.setMinimumSize(QtCore.QSize(185, 30))
        self.label_36.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_35.addWidget(self.label_36)
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem50)
        self.gridLayout_18.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame_16, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_14, 1, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.stockSettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_35 = QtWidgets.QLabel(self.frame_13)
        self.label_35.setMinimumSize(QtCore.QSize(185, 30))
        self.label_35.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout_36.addWidget(self.label_35)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem51)
        self.gridLayout_19.addLayout(self.horizontalLayout_36, 0, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.frame_13)
        self.label_45.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_45.setStyleSheet("background-color: #63b946;")
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.gridLayout_19.addWidget(self.label_45, 2, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet("background-color:rgb(230, 240, 230)")
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_22.setObjectName("gridLayout_22")
        spacerItem52 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem52, 2, 1, 1, 1)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setContentsMargins(0, 0, 0, -1)
        self.formLayout_8.setVerticalSpacing(10)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_46 = QtWidgets.QLabel(self.frame_19)
        self.label_46.setMinimumSize(QtCore.QSize(135, 30))
        self.label_46.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.editItemChooseItemComboBox = QtWidgets.QComboBox(self.frame_19)
        self.editItemChooseItemComboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.editItemChooseItemComboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemChooseItemComboBox.setFont(font)
        self.editItemChooseItemComboBox.setStyleSheet("color: rgb(46, 52, 54);\n"
"background-color: rgb(255, 255, 255);")
        self.editItemChooseItemComboBox.setEditable(True)
        self.editItemChooseItemComboBox.setObjectName("editItemChooseItemComboBox")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editItemChooseItemComboBox)
        self.label_47 = QtWidgets.QLabel(self.frame_19)
        self.label_47.setMinimumSize(QtCore.QSize(135, 30))
        self.label_47.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.editItemCurrentQtyLineEdit = QtWidgets.QLineEdit(self.frame_19)
        self.editItemCurrentQtyLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editItemCurrentQtyLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemCurrentQtyLineEdit.setFont(font)
        self.editItemCurrentQtyLineEdit.setStyleSheet("border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.editItemCurrentQtyLineEdit.setReadOnly(True)
        self.editItemCurrentQtyLineEdit.setObjectName("editItemCurrentQtyLineEdit")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editItemCurrentQtyLineEdit)
        self.label_48 = QtWidgets.QLabel(self.frame_19)
        self.label_48.setMinimumSize(QtCore.QSize(135, 30))
        self.label_48.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_52 = QtWidgets.QLabel(self.frame_19)
        self.label_52.setMinimumSize(QtCore.QSize(40, 30))
        self.label_52.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_41.addWidget(self.label_52)
        self.editItemCurrentUnitPriceLineEdit = QtWidgets.QLineEdit(self.frame_19)
        self.editItemCurrentUnitPriceLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.editItemCurrentUnitPriceLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemCurrentUnitPriceLineEdit.setFont(font)
        self.editItemCurrentUnitPriceLineEdit.setStyleSheet("\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.editItemCurrentUnitPriceLineEdit.setReadOnly(True)
        self.editItemCurrentUnitPriceLineEdit.setObjectName("editItemCurrentUnitPriceLineEdit")
        self.horizontalLayout_41.addWidget(self.editItemCurrentUnitPriceLineEdit)
        self.formLayout_8.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_41)
        self.label_49 = QtWidgets.QLabel(self.frame_19)
        self.label_49.setMinimumSize(QtCore.QSize(135, 30))
        self.label_49.setMaximumSize(QtCore.QSize(135, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.editItemAddQtySpinBox = QtWidgets.QSpinBox(self.frame_19)
        self.editItemAddQtySpinBox.setMinimumSize(QtCore.QSize(135, 30))
        self.editItemAddQtySpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemAddQtySpinBox.setFont(font)
        self.editItemAddQtySpinBox.setStyleSheet("background-color:#ffffff;")
        self.editItemAddQtySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.editItemAddQtySpinBox.setMinimum(-2145778999)
        self.editItemAddQtySpinBox.setMaximum(2145778999)
        self.editItemAddQtySpinBox.setProperty("value", 0)
        self.editItemAddQtySpinBox.setObjectName("editItemAddQtySpinBox")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editItemAddQtySpinBox)
        self.label_53 = QtWidgets.QLabel(self.frame_19)
        self.label_53.setMinimumSize(QtCore.QSize(135, 30))
        self.label_53.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_54 = QtWidgets.QLabel(self.frame_19)
        self.label_54.setMinimumSize(QtCore.QSize(40, 30))
        self.label_54.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background-color: #ffffff;")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_42.addWidget(self.label_54)
        self.editItemNewUnitPriceSpinBox = QtWidgets.QDoubleSpinBox(self.frame_19)
        self.editItemNewUnitPriceSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.editItemNewUnitPriceSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemNewUnitPriceSpinBox.setFont(font)
        self.editItemNewUnitPriceSpinBox.setStyleSheet("background-color: rgb(255, 255, 255, 255);")
        self.editItemNewUnitPriceSpinBox.setFrame(False)
        self.editItemNewUnitPriceSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.editItemNewUnitPriceSpinBox.setMaximum(1e+16)
        self.editItemNewUnitPriceSpinBox.setObjectName("editItemNewUnitPriceSpinBox")
        self.horizontalLayout_42.addWidget(self.editItemNewUnitPriceSpinBox)
        self.formLayout_8.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_42)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_43.addItem(spacerItem53)
        self.editItemClearButton = QtWidgets.QPushButton(self.frame_19)
        self.editItemClearButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editItemClearButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemClearButton.setFont(font)
        self.editItemClearButton.setStyleSheet("QPushButton#editItemClearButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editItemClearButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editItemClearButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editItemClearButton.setObjectName("editItemClearButton")
        self.horizontalLayout_43.addWidget(self.editItemClearButton)
        self.editItemUpdateButton = QtWidgets.QPushButton(self.frame_19)
        self.editItemUpdateButton.setMinimumSize(QtCore.QSize(100, 30))
        self.editItemUpdateButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editItemUpdateButton.setFont(font)
        self.editItemUpdateButton.setStyleSheet("QPushButton#editItemUpdateButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#editItemUpdateButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#editItemUpdateButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.editItemUpdateButton.setObjectName("editItemUpdateButton")
        self.horizontalLayout_43.addWidget(self.editItemUpdateButton)
        self.formLayout_8.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_43)
        self.gridLayout_22.addLayout(self.formLayout_8, 1, 1, 1, 1)
        spacerItem54 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem54, 1, 2, 1, 1)
        spacerItem55 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_22.addItem(spacerItem55, 0, 1, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem56, 1, 0, 1, 1)
        self.gridLayout_19.addWidget(self.frame_19, 3, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_13, 1, 1, 1, 1)
        self.settingsStackedWidget.addWidget(self.stockSettingsPage)
        self.otherSettingsPage = QtWidgets.QWidget()
        self.otherSettingsPage.setObjectName("otherSettingsPage")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.otherSettingsPage)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setHorizontalSpacing(5)
        self.gridLayout_23.setVerticalSpacing(2)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.frame_20 = QtWidgets.QFrame(self.otherSettingsPage)
        self.frame_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_55 = QtWidgets.QLabel(self.frame_20)
        self.label_55.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_55.setStyleSheet("background-color: #63b946;")
        self.label_55.setText("")
        self.label_55.setObjectName("label_55")
        self.gridLayout_24.addWidget(self.label_55, 2, 0, 1, 1)
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.label_56 = QtWidgets.QLabel(self.frame_20)
        self.label_56.setMinimumSize(QtCore.QSize(185, 30))
        self.label_56.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_45.addWidget(self.label_56)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_45.addItem(spacerItem57)
        self.gridLayout_24.addLayout(self.horizontalLayout_45, 0, 0, 1, 1)
        self.frame_24 = QtWidgets.QFrame(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_24.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_24.setObjectName("frame_24")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_24)
        self.gridLayout_25.setObjectName("gridLayout_25")
        spacerItem58 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem58, 2, 3, 1, 1)
        spacerItem59 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_25.addItem(spacerItem59, 1, 1, 1, 2)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setContentsMargins(0, 0, 0, 0)
        self.formLayout_9.setHorizontalSpacing(0)
        self.formLayout_9.setVerticalSpacing(10)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_60 = QtWidgets.QLabel(self.frame_24)
        self.label_60.setMinimumSize(QtCore.QSize(0, 30))
        self.label_60.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_60.setFont(font)
        self.label_60.setWordWrap(False)
        self.label_60.setObjectName("label_60")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_60)
        self.notificationMinQtyOfItemsToNotifySpinBox = QtWidgets.QSpinBox(self.frame_24)
        self.notificationMinQtyOfItemsToNotifySpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.notificationMinQtyOfItemsToNotifySpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.notificationMinQtyOfItemsToNotifySpinBox.setFont(font)
        self.notificationMinQtyOfItemsToNotifySpinBox.setStyleSheet("background-color:#ffffff;")
        self.notificationMinQtyOfItemsToNotifySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.notificationMinQtyOfItemsToNotifySpinBox.setMinimum(10)
        self.notificationMinQtyOfItemsToNotifySpinBox.setMaximum(1000000000)
        self.notificationMinQtyOfItemsToNotifySpinBox.setObjectName("notificationMinQtyOfItemsToNotifySpinBox")
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.notificationMinQtyOfItemsToNotifySpinBox)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem60)
        self.saveNotifSettingsButton = QtWidgets.QPushButton(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveNotifSettingsButton.sizePolicy().hasHeightForWidth())
        self.saveNotifSettingsButton.setSizePolicy(sizePolicy)
        self.saveNotifSettingsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.saveNotifSettingsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveNotifSettingsButton.setFont(font)
        self.saveNotifSettingsButton.setStyleSheet("QPushButton#saveNotifSettingsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#saveNotifSettingsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#saveNotifSettingsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.saveNotifSettingsButton.setObjectName("saveNotifSettingsButton")
        self.horizontalLayout_30.addWidget(self.saveNotifSettingsButton)
        self.formLayout_9.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_30)
        self.gridLayout_25.addLayout(self.formLayout_9, 2, 1, 1, 2)
        spacerItem61 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_25.addItem(spacerItem61, 2, 0, 1, 1)
        self.gridLayout_24.addWidget(self.frame_24, 3, 0, 1, 1)
        self.gridLayout_23.addWidget(self.frame_20, 0, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.otherSettingsPage)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.frame_22 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.formLayout_11 = QtWidgets.QFormLayout()
        self.formLayout_11.setVerticalSpacing(10)
        self.formLayout_11.setObjectName("formLayout_11")
        self.firmNameLabel = QtWidgets.QLabel(self.frame_22)
        self.firmNameLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmNameLabel.setFont(font)
        self.firmNameLabel.setObjectName("firmNameLabel")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firmNameLabel)
        self.firmNameLineEdit = QtWidgets.QLineEdit(self.frame_22)
        self.firmNameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmNameLineEdit.setFont(font)
        self.firmNameLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.firmNameLineEdit.setObjectName("firmNameLineEdit")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firmNameLineEdit)
        self.firmContactLabel = QtWidgets.QLabel(self.frame_22)
        self.firmContactLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmContactLabel.setFont(font)
        self.firmContactLabel.setObjectName("firmContactLabel")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firmContactLabel)
        self.firmContactLineEdit = QtWidgets.QLineEdit(self.frame_22)
        self.firmContactLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmContactLineEdit.setFont(font)
        self.firmContactLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.firmContactLineEdit.setObjectName("firmContactLineEdit")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firmContactLineEdit)
        self.firmAddressLabel = QtWidgets.QLabel(self.frame_22)
        self.firmAddressLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmAddressLabel.setFont(font)
        self.firmAddressLabel.setObjectName("firmAddressLabel")
        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.firmAddressLabel)
        self.firmAddressLineEdit = QtWidgets.QLineEdit(self.frame_22)
        self.firmAddressLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.firmAddressLineEdit.setFont(font)
        self.firmAddressLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"padding-left:5px;\n"
"padding-right: 5px;\n"
"")
        self.firmAddressLineEdit.setObjectName("firmAddressLineEdit")
        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.firmAddressLineEdit)
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem62)
        self.clearFirmInfoButton = QtWidgets.QPushButton(self.frame_22)
        self.clearFirmInfoButton.setMinimumSize(QtCore.QSize(100, 30))
        self.clearFirmInfoButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearFirmInfoButton.setFont(font)
        self.clearFirmInfoButton.setStyleSheet("QPushButton#clearFirmInfoButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#clearFirmInfoButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#clearFirmInfoButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.clearFirmInfoButton.setObjectName("clearFirmInfoButton")
        self.horizontalLayout_57.addWidget(self.clearFirmInfoButton)
        self.loadFirmInfoButton = QtWidgets.QPushButton(self.frame_22)
        self.loadFirmInfoButton.setMinimumSize(QtCore.QSize(100, 30))
        self.loadFirmInfoButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loadFirmInfoButton.setFont(font)
        self.loadFirmInfoButton.setStyleSheet("QPushButton#loadFirmInfoButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#loadFirmInfoButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#loadFirmInfoButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.loadFirmInfoButton.setObjectName("loadFirmInfoButton")
        self.horizontalLayout_57.addWidget(self.loadFirmInfoButton)
        self.updateFirmInfoButton = QtWidgets.QPushButton(self.frame_22)
        self.updateFirmInfoButton.setMinimumSize(QtCore.QSize(100, 30))
        self.updateFirmInfoButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.updateFirmInfoButton.setFont(font)
        self.updateFirmInfoButton.setStyleSheet("QPushButton#updateFirmInfoButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#updateFirmInfoButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#updateFirmInfoButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.updateFirmInfoButton.setObjectName("updateFirmInfoButton")
        self.horizontalLayout_57.addWidget(self.updateFirmInfoButton)
        self.formLayout_11.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_57)
        self.gridLayout_31.addLayout(self.formLayout_11, 1, 1, 1, 1)
        spacerItem63 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem63, 1, 0, 1, 1)
        spacerItem64 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_31.addItem(spacerItem64, 0, 1, 1, 1)
        spacerItem65 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_31.addItem(spacerItem65, 1, 2, 1, 1)
        spacerItem66 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_31.addItem(spacerItem66, 2, 1, 1, 1)
        self.gridLayout_27.addWidget(self.frame_22, 2, 0, 1, 1)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_62 = QtWidgets.QLabel(self.frame_10)
        self.label_62.setMinimumSize(QtCore.QSize(185, 30))
        self.label_62.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_55.addWidget(self.label_62)
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem67)
        self.gridLayout_27.addLayout(self.horizontalLayout_55, 0, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.frame_10)
        self.label_61.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_61.setStyleSheet("background-color: #63b946;")
        self.label_61.setText("")
        self.label_61.setObjectName("label_61")
        self.gridLayout_27.addWidget(self.label_61, 1, 0, 1, 1)
        self.gridLayout_23.addWidget(self.frame_10, 1, 0, 1, 1)
        self.frame_21 = QtWidgets.QFrame(self.otherSettingsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setHorizontalSpacing(6)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frame_25 = QtWidgets.QFrame(self.frame_21)
        self.frame_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_25.setObjectName("frame_25")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.frame_25)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.label_57 = QtWidgets.QLabel(self.frame_25)
        self.label_57.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_57.setStyleSheet("background-color: #63b946;")
        self.label_57.setText("")
        self.label_57.setObjectName("label_57")
        self.gridLayout_26.addWidget(self.label_57, 2, 0, 1, 1)
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_58 = QtWidgets.QLabel(self.frame_25)
        self.label_58.setMinimumSize(QtCore.QSize(185, 30))
        self.label_58.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.horizontalLayout_46.addWidget(self.label_58)
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem68)
        self.gridLayout_26.addLayout(self.horizontalLayout_46, 0, 0, 1, 1)
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_26.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_29.setVerticalSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.formLayout_10 = QtWidgets.QFormLayout()
        self.formLayout_10.setLabelAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setVerticalSpacing(10)
        self.formLayout_10.setObjectName("formLayout_10")
        self.backupDataTurnOnOffAutoBackupCheckBox = QtWidgets.QCheckBox(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backupDataTurnOnOffAutoBackupCheckBox.sizePolicy().hasHeightForWidth())
        self.backupDataTurnOnOffAutoBackupCheckBox.setSizePolicy(sizePolicy)
        self.backupDataTurnOnOffAutoBackupCheckBox.setMinimumSize(QtCore.QSize(0, 30))
        self.backupDataTurnOnOffAutoBackupCheckBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backupDataTurnOnOffAutoBackupCheckBox.setFont(font)
        self.backupDataTurnOnOffAutoBackupCheckBox.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #ffffff;\n"
"width : 20px;\n"
"height: 20px;\n"
"\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"background-color:#63b946;\n"
"}")
        self.backupDataTurnOnOffAutoBackupCheckBox.setObjectName("backupDataTurnOnOffAutoBackupCheckBox")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.backupDataTurnOnOffAutoBackupCheckBox)
        self.label_59 = QtWidgets.QLabel(self.frame_26)
        self.label_59.setMinimumSize(QtCore.QSize(0, 30))
        self.label_59.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.backupDataTimeIntervalSpinBox = QtWidgets.QSpinBox(self.frame_26)
        self.backupDataTimeIntervalSpinBox.setMinimumSize(QtCore.QSize(100, 30))
        self.backupDataTimeIntervalSpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backupDataTimeIntervalSpinBox.setFont(font)
        self.backupDataTimeIntervalSpinBox.setStyleSheet("background-color:#ffffff;")
        self.backupDataTimeIntervalSpinBox.setFrame(True)
        self.backupDataTimeIntervalSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.backupDataTimeIntervalSpinBox.setMinimum(1)
        self.backupDataTimeIntervalSpinBox.setMaximum(720)
        self.backupDataTimeIntervalSpinBox.setProperty("value", 1)
        self.backupDataTimeIntervalSpinBox.setObjectName("backupDataTimeIntervalSpinBox")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.backupDataTimeIntervalSpinBox)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setContentsMargins(-1, 20, -1, 0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem69)
        self.saveBackupSettingsButton = QtWidgets.QPushButton(self.frame_26)
        self.saveBackupSettingsButton.setMinimumSize(QtCore.QSize(100, 30))
        self.saveBackupSettingsButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveBackupSettingsButton.setFont(font)
        self.saveBackupSettingsButton.setStyleSheet("QPushButton#saveBackupSettingsButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#saveBackupSettingsButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#saveBackupSettingsButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.saveBackupSettingsButton.setObjectName("saveBackupSettingsButton")
        self.horizontalLayout_49.addWidget(self.saveBackupSettingsButton)
        self.formLayout_10.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_49)
        self.line = QtWidgets.QFrame(self.frame_26)
        self.line.setMinimumSize(QtCore.QSize(50, 10))
        self.line.setMaximumSize(QtCore.QSize(16777215, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        spacerItem70 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem70)
        self.backupDataBackupNowButton = QtWidgets.QPushButton(self.frame_26)
        self.backupDataBackupNowButton.setMinimumSize(QtCore.QSize(200, 50))
        self.backupDataBackupNowButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.backupDataBackupNowButton.setFont(font)
        self.backupDataBackupNowButton.setStyleSheet("QPushButton#backupDataBackupNowButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#backupDataBackupNowButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#backupDataBackupNowButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.backupDataBackupNowButton.setObjectName("backupDataBackupNowButton")
        self.horizontalLayout_48.addWidget(self.backupDataBackupNowButton)
        spacerItem71 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem71)
        self.formLayout_10.setLayout(5, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_48)
        self.backupAnimLabel = QtWidgets.QLabel(self.frame_26)
        self.backupAnimLabel.setMinimumSize(QtCore.QSize(50, 40))
        self.backupAnimLabel.setText("")
        self.backupAnimLabel.setScaledContents(False)
        self.backupAnimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.backupAnimLabel.setObjectName("backupAnimLabel")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.backupAnimLabel)
        self.gridLayout_29.addLayout(self.formLayout_10, 1, 1, 1, 1)
        spacerItem72 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_29.addItem(spacerItem72, 0, 1, 1, 1)
        spacerItem73 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem73, 1, 0, 1, 1)
        spacerItem74 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem74, 1, 2, 1, 1)
        self.gridLayout_26.addWidget(self.frame_26, 3, 0, 1, 1)
        self.gridLayout_28.addWidget(self.frame_25, 0, 0, 1, 1)
        self.gridLayout_23.addWidget(self.frame_21, 0, 1, 1, 1)
        self.frame_23 = QtWidgets.QFrame(self.otherSettingsPage)
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_63 = QtWidgets.QLabel(self.frame_23)
        self.label_63.setMinimumSize(QtCore.QSize(185, 30))
        self.label_63.setMaximumSize(QtCore.QSize(185, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("background-color: #63b946;\n"
"color: #ffffff;\n"
"padding: 3px;")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_56.addWidget(self.label_63)
        spacerItem75 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem75)
        self.verticalLayout_17.addLayout(self.horizontalLayout_56)
        self.label_64 = QtWidgets.QLabel(self.frame_23)
        self.label_64.setMaximumSize(QtCore.QSize(16777215, 1))
        self.label_64.setStyleSheet("background-color: #63b946;")
        self.label_64.setText("")
        self.label_64.setObjectName("label_64")
        self.verticalLayout_17.addWidget(self.label_64)
        self.frame_27 = QtWidgets.QFrame(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setStyleSheet("background-color:rgb(230, 240, 230);")
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_27.setObjectName("frame_27")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.frame_27)
        self.gridLayout_30.setObjectName("gridLayout_30")
        spacerItem76 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem76, 1, 0, 1, 1)
        self.restoreDataButton = QtWidgets.QPushButton(self.frame_27)
        self.restoreDataButton.setMinimumSize(QtCore.QSize(200, 50))
        self.restoreDataButton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.restoreDataButton.setFont(font)
        self.restoreDataButton.setStyleSheet("QPushButton#restoreDataButton{\n"
"    color: #ffffff;\n"
"    background-color: #63b946;\n"
"    border: 0px;\n"
"    padding-right: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"QPushButton#restoreDataButton:hover{\n"
"    color: #000000;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#restoreDataButton:pressed{\n"
"    color: #000000;\n"
"    background-color: #f2f2f2;\n"
"}")
        self.restoreDataButton.setObjectName("restoreDataButton")
        self.gridLayout_30.addWidget(self.restoreDataButton, 1, 1, 1, 1)
        spacerItem77 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_30.addItem(spacerItem77, 0, 1, 1, 1)
        spacerItem78 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_30.addItem(spacerItem78, 3, 1, 1, 1)
        spacerItem79 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem79, 1, 2, 1, 1)
        self.restoreDataAnimLabel = QtWidgets.QLabel(self.frame_27)
        self.restoreDataAnimLabel.setMinimumSize(QtCore.QSize(50, 40))
        self.restoreDataAnimLabel.setText("")
        self.restoreDataAnimLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.restoreDataAnimLabel.setObjectName("restoreDataAnimLabel")
        self.gridLayout_30.addWidget(self.restoreDataAnimLabel, 2, 0, 1, 3)
        self.verticalLayout_17.addWidget(self.frame_27)
        self.gridLayout_23.addWidget(self.frame_23, 1, 1, 1, 1)
        self.settingsStackedWidget.addWidget(self.otherSettingsPage)
        self.gridLayout_2.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.contentStackedWidget.addWidget(self.settingsPage)
        self.verticalLayout.addWidget(self.contentStackedWidget)
        SMSMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SMSMainWindow)
        self.contentStackedWidget.setCurrentIndex(0)
        self.settingsStackedWidget.setCurrentIndex(0)
        self.editSalesPersonUsernameComboBox.setCurrentIndex(-1)
        self.removeSalesPersonUsernameComboBox.setCurrentIndex(-1)
        self.addSalesPersonClearButton.clicked.connect(self.addSalesPersonConfirmPasswordLineEdit.clear)
        self.addSalesPersonClearButton.clicked.connect(self.addSalesPersonPasswordLineEdit.clear)
        self.addSalesPersonClearButton.clicked.connect(self.addSalesPersonUsernameLineEdit.clear)
        self.editSalesPerosnCancelButton.clicked.connect(self.editSalesPersonConfirmNewPasswordLineEdit.clear)
        self.editSalesPerosnCancelButton.clicked.connect(self.editSalesPersonNewPasswordLineEdit.clear)
        self.editSalesPerosnCancelButton.clicked.connect(self.editSalesPersonCurrentPasswordLineEdit.clear)
        self.editSalesPerosnCancelButton.clicked.connect(self.editSalesPersonNewUsernameLineEdit.clear)
        self.editSalesPerosnCancelButton.clicked.connect(self.editSalesPersonUsernameComboBox.clearEditText)
        self.removeSalesPersonRevokeButton.clicked.connect(self.removeSalesPersonUsernameComboBox.clearEditText)
        self.editAdminCancelButton.clicked.connect(self.editAdminConfirmPasswordLineEdit.clear)
        self.editAdminCancelButton.clicked.connect(self.editAdminNewPasswordLineEdit.clear)
        self.editAdminCancelButton.clicked.connect(self.editAdminCurrentPasswordLineEdit.clear)
        self.editSalesPersonUsernameComboBox.currentTextChanged['QString'].connect(self.editSalesPersonNewUsernameLineEdit.setText)
        self.removeItemClearButton.clicked.connect(self.removeItemQtyLineEdit.clear)
        self.removeItemClearButton.clicked.connect(self.removeItemUnitPriceLineEdit.clear)
        self.removeItemClearButton.clicked.connect(self.removeItemChooseItemComboBox.clearEditText)
        self.clearFirmInfoButton.clicked.connect(self.firmNameLineEdit.clear)
        self.clearFirmInfoButton.clicked.connect(self.firmContactLineEdit.clear)
        self.clearFirmInfoButton.clicked.connect(self.firmAddressLineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(SMSMainWindow)
        SMSMainWindow.setTabOrder(self.salesPointScrollArea, self.salesItemComboBox)
        SMSMainWindow.setTabOrder(self.salesItemComboBox, self.salesQtyOfItemsSpinBox)
        SMSMainWindow.setTabOrder(self.salesQtyOfItemsSpinBox, self.ghanaCediSymboLineEdit)
        SMSMainWindow.setTabOrder(self.ghanaCediSymboLineEdit, self.totalCostForSelectedItemLineEdit)
        SMSMainWindow.setTabOrder(self.totalCostForSelectedItemLineEdit, self.itemQtyLeftLineEdit)
        SMSMainWindow.setTabOrder(self.itemQtyLeftLineEdit, self.addToCartButton)
        SMSMainWindow.setTabOrder(self.addToCartButton, self.cartTableWidget)
        SMSMainWindow.setTabOrder(self.cartTableWidget, self.removeFromCartButton)
        SMSMainWindow.setTabOrder(self.removeFromCartButton, self.salesGhanaCediSymboLineEdit)
        SMSMainWindow.setTabOrder(self.salesGhanaCediSymboLineEdit, self.salesTotalCostLineEdit)
        SMSMainWindow.setTabOrder(self.salesTotalCostLineEdit, self.reloadItemsButton)
        SMSMainWindow.setTabOrder(self.reloadItemsButton, self.sellButton)
        SMSMainWindow.setTabOrder(self.sellButton, self.salesResetAllButton)
        SMSMainWindow.setTabOrder(self.salesResetAllButton, self.salesPrintReceiptButton)
        SMSMainWindow.setTabOrder(self.salesPrintReceiptButton, self.salesSearchDateEdit)
        SMSMainWindow.setTabOrder(self.salesSearchDateEdit, self.salesSearchParamComboBox)
        SMSMainWindow.setTabOrder(self.salesSearchParamComboBox, self.salesSearchField)
        SMSMainWindow.setTabOrder(self.salesSearchField, self.salesSearchButton)
        SMSMainWindow.setTabOrder(self.salesSearchButton, self.salesSortComboBox)
        SMSMainWindow.setTabOrder(self.salesSortComboBox, self.salesFlipTableButton)
        SMSMainWindow.setTabOrder(self.salesFlipTableButton, self.salesLoadTableButton)
        SMSMainWindow.setTabOrder(self.salesLoadTableButton, self.salesPrevSearchButton)
        SMSMainWindow.setTabOrder(self.salesPrevSearchButton, self.salesNextSearchButton)
        SMSMainWindow.setTabOrder(self.salesNextSearchButton, self.salesRecordsTableWidget)
        SMSMainWindow.setTabOrder(self.salesRecordsTableWidget, self.viewNotifTextEdit)
        SMSMainWindow.setTabOrder(self.viewNotifTextEdit, self.recordsDailyMonthComboBox)
        SMSMainWindow.setTabOrder(self.recordsDailyMonthComboBox, self.recordsDailyYearSpinBox)
        SMSMainWindow.setTabOrder(self.recordsDailyYearSpinBox, self.dailyRecordsViewButton)
        SMSMainWindow.setTabOrder(self.dailyRecordsViewButton, self.recordsMonthlyYearSpinBox)
        SMSMainWindow.setTabOrder(self.recordsMonthlyYearSpinBox, self.monthlyRecordsViewButton)
        SMSMainWindow.setTabOrder(self.monthlyRecordsViewButton, self.recordsYearlyFromYearSpinBox)
        SMSMainWindow.setTabOrder(self.recordsYearlyFromYearSpinBox, self.recordsYearlyToYearSpinBox)
        SMSMainWindow.setTabOrder(self.recordsYearlyToYearSpinBox, self.yearlyRecordsViewButton)
        SMSMainWindow.setTabOrder(self.yearlyRecordsViewButton, self.recordsSearchDateEdit)
        SMSMainWindow.setTabOrder(self.recordsSearchDateEdit, self.recordsSearchParamComboBox)
        SMSMainWindow.setTabOrder(self.recordsSearchParamComboBox, self.recordsSearchField)
        SMSMainWindow.setTabOrder(self.recordsSearchField, self.recordsSearchButton)
        SMSMainWindow.setTabOrder(self.recordsSearchButton, self.recordsSortComboBox)
        SMSMainWindow.setTabOrder(self.recordsSortComboBox, self.recordsFlipTableButton)
        SMSMainWindow.setTabOrder(self.recordsFlipTableButton, self.recordsLoadTableButton)
        SMSMainWindow.setTabOrder(self.recordsLoadTableButton, self.recordsPrevSearchButton)
        SMSMainWindow.setTabOrder(self.recordsPrevSearchButton, self.recordsNextSearchButton)
        SMSMainWindow.setTabOrder(self.recordsNextSearchButton, self.recordsTableWidget)
        SMSMainWindow.setTabOrder(self.recordsTableWidget, self.addSalesPersonUsernameLineEdit)
        SMSMainWindow.setTabOrder(self.addSalesPersonUsernameLineEdit, self.addSalesPersonPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.addSalesPersonPasswordLineEdit, self.addSalesPersonHideShowPasswordButton)
        SMSMainWindow.setTabOrder(self.addSalesPersonHideShowPasswordButton, self.addSalesPersonConfirmPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.addSalesPersonConfirmPasswordLineEdit, self.addSalesPersonShowHideConfirmPasswordButton)
        SMSMainWindow.setTabOrder(self.addSalesPersonShowHideConfirmPasswordButton, self.addSalesPersonClearButton)
        SMSMainWindow.setTabOrder(self.addSalesPersonClearButton, self.addSalesPersonSubmitButton)
        SMSMainWindow.setTabOrder(self.addSalesPersonSubmitButton, self.viewAllSalesPersonsButton)
        SMSMainWindow.setTabOrder(self.viewAllSalesPersonsButton, self.removeSalesPersonUsernameComboBox)
        SMSMainWindow.setTabOrder(self.removeSalesPersonUsernameComboBox, self.removeSalesPersonRevokeButton)
        SMSMainWindow.setTabOrder(self.removeSalesPersonRevokeButton, self.removeSalesPersonConfirmButton)
        SMSMainWindow.setTabOrder(self.removeSalesPersonConfirmButton, self.editSalesPersonUsernameComboBox)
        SMSMainWindow.setTabOrder(self.editSalesPersonUsernameComboBox, self.editSalesPersonNewUsernameLineEdit)
        SMSMainWindow.setTabOrder(self.editSalesPersonNewUsernameLineEdit, self.editSalesPersonCurrentPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editSalesPersonCurrentPasswordLineEdit, self.editSalesPersonShowHideCurrentPasswordButton)
        SMSMainWindow.setTabOrder(self.editSalesPersonShowHideCurrentPasswordButton, self.editSalesPersonNewPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editSalesPersonNewPasswordLineEdit, self.editSalesPersonShowHideNewPasswordButton)
        SMSMainWindow.setTabOrder(self.editSalesPersonShowHideNewPasswordButton, self.editSalesPersonConfirmNewPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editSalesPersonConfirmNewPasswordLineEdit, self.editSalesPersonShowHideConfirmPasswordButton)
        SMSMainWindow.setTabOrder(self.editSalesPersonShowHideConfirmPasswordButton, self.editSalesPerosnCancelButton)
        SMSMainWindow.setTabOrder(self.editSalesPerosnCancelButton, self.editSalesPersonSaveButton)
        SMSMainWindow.setTabOrder(self.editSalesPersonSaveButton, self.editAdminNameLineEdit)
        SMSMainWindow.setTabOrder(self.editAdminNameLineEdit, self.editAdminCurrentPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editAdminCurrentPasswordLineEdit, self.editAdminShowHideCurrentPasswordButton)
        SMSMainWindow.setTabOrder(self.editAdminShowHideCurrentPasswordButton, self.editAdminNewPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editAdminNewPasswordLineEdit, self.editAdminShowHideNewPasswordButton)
        SMSMainWindow.setTabOrder(self.editAdminShowHideNewPasswordButton, self.editAdminConfirmPasswordLineEdit)
        SMSMainWindow.setTabOrder(self.editAdminConfirmPasswordLineEdit, self.editAdminShowHideConfirmPasswordButton)
        SMSMainWindow.setTabOrder(self.editAdminShowHideConfirmPasswordButton, self.editAdminCancelButton)
        SMSMainWindow.setTabOrder(self.editAdminCancelButton, self.editAdminSaveButton)
        SMSMainWindow.setTabOrder(self.editAdminSaveButton, self.addNewItemDescLineEdit)
        SMSMainWindow.setTabOrder(self.addNewItemDescLineEdit, self.addNewItemUnitPriceSpinBox)
        SMSMainWindow.setTabOrder(self.addNewItemUnitPriceSpinBox, self.addNewItemQtySpinBox)
        SMSMainWindow.setTabOrder(self.addNewItemQtySpinBox, self.addNewItemClearButton)
        SMSMainWindow.setTabOrder(self.addNewItemClearButton, self.addNewItemAddButton)
        SMSMainWindow.setTabOrder(self.addNewItemAddButton, self.viewAllItemsButton)
        SMSMainWindow.setTabOrder(self.viewAllItemsButton, self.removeItemChooseItemComboBox)
        SMSMainWindow.setTabOrder(self.removeItemChooseItemComboBox, self.removeItemUnitPriceLineEdit)
        SMSMainWindow.setTabOrder(self.removeItemUnitPriceLineEdit, self.removeItemQtyLineEdit)
        SMSMainWindow.setTabOrder(self.removeItemQtyLineEdit, self.removeItemClearButton)
        SMSMainWindow.setTabOrder(self.removeItemClearButton, self.removeItemRemoveButton)
        SMSMainWindow.setTabOrder(self.removeItemRemoveButton, self.editItemChooseItemComboBox)
        SMSMainWindow.setTabOrder(self.editItemChooseItemComboBox, self.editItemCurrentQtyLineEdit)
        SMSMainWindow.setTabOrder(self.editItemCurrentQtyLineEdit, self.editItemCurrentUnitPriceLineEdit)
        SMSMainWindow.setTabOrder(self.editItemCurrentUnitPriceLineEdit, self.editItemAddQtySpinBox)
        SMSMainWindow.setTabOrder(self.editItemAddQtySpinBox, self.editItemNewUnitPriceSpinBox)
        SMSMainWindow.setTabOrder(self.editItemNewUnitPriceSpinBox, self.editItemClearButton)
        SMSMainWindow.setTabOrder(self.editItemClearButton, self.editItemUpdateButton)
        SMSMainWindow.setTabOrder(self.editItemUpdateButton, self.notificationMinQtyOfItemsToNotifySpinBox)
        SMSMainWindow.setTabOrder(self.notificationMinQtyOfItemsToNotifySpinBox, self.saveNotifSettingsButton)
        SMSMainWindow.setTabOrder(self.saveNotifSettingsButton, self.backupDataTurnOnOffAutoBackupCheckBox)
        SMSMainWindow.setTabOrder(self.backupDataTurnOnOffAutoBackupCheckBox, self.backupDataTimeIntervalSpinBox)
        SMSMainWindow.setTabOrder(self.backupDataTimeIntervalSpinBox, self.saveBackupSettingsButton)
        SMSMainWindow.setTabOrder(self.saveBackupSettingsButton, self.backupDataBackupNowButton)
        SMSMainWindow.setTabOrder(self.backupDataBackupNowButton, self.firmNameLineEdit)
        SMSMainWindow.setTabOrder(self.firmNameLineEdit, self.firmContactLineEdit)
        SMSMainWindow.setTabOrder(self.firmContactLineEdit, self.firmAddressLineEdit)
        SMSMainWindow.setTabOrder(self.firmAddressLineEdit, self.clearFirmInfoButton)
        SMSMainWindow.setTabOrder(self.clearFirmInfoButton, self.loadFirmInfoButton)
        SMSMainWindow.setTabOrder(self.loadFirmInfoButton, self.updateFirmInfoButton)
        SMSMainWindow.setTabOrder(self.updateFirmInfoButton, self.restoreDataButton)

    def retranslateUi(self, SMSMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SMSMainWindow.setWindowTitle(_translate("SMSMainWindow", "Sales Management System"))
        self.salesMenuButton.setText(_translate("SMSMainWindow", "SALES"))
        self.notifMenuButton.setText(_translate("SMSMainWindow", "NOTIFICATIONS"))
        self.recordsMenuButton.setText(_translate("SMSMainWindow", "RECORDS"))
        self.settingsMenuButton.setText(_translate("SMSMainWindow", "SETTINGS"))
        self.backupMenuButton.setToolTip(_translate("SMSMainWindow", "Back Up"))
        self.logoutMenuButton.setToolTip(_translate("SMSMainWindow", "Log Out"))
        self.salesItemLabel_2.setText(_translate("SMSMainWindow", "Item:"))
        self.salesQtyOfItemsLabel_2.setText(_translate("SMSMainWindow", "    Quantity:      "))
        self.totalCostForSelectedItemLabel.setText(_translate("SMSMainWindow", " Cost Of Item(s)"))
        self.label_9.setText(_translate("SMSMainWindow", " = "))
        self.ghanaCediSymboLineEdit.setText(_translate("SMSMainWindow", "GH₵"))
        self.totalCostForSelectedItemLineEdit.setText(_translate("SMSMainWindow", "0.00"))
        self.qtyLeftLabel.setText(_translate("SMSMainWindow", " Quantity Left"))
        self.label_12.setText(_translate("SMSMainWindow", " = "))
        self.itemQtyLeftLineEdit.setText(_translate("SMSMainWindow", "0"))
        self.addToCartButton.setText(_translate("SMSMainWindow", "Add To Cart"))
        item = self.cartTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SMSMainWindow", "ITEM"))
        item = self.cartTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SMSMainWindow", "QUANTITY"))
        item = self.cartTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SMSMainWindow", "COST (GH₵)"))
        self.removeFromCartButton.setText(_translate("SMSMainWindow", "Remove From Cart"))
        self.salesTotalCostLabel.setText(_translate("SMSMainWindow", "  Total Cost ="))
        self.salesGhanaCediSymboLineEdit.setText(_translate("SMSMainWindow", "GH₵"))
        self.salesTotalCostLineEdit.setText(_translate("SMSMainWindow", "0.00"))
        self.reloadItemsButton.setText(_translate("SMSMainWindow", "Reload Items"))
        self.sellButton.setText(_translate("SMSMainWindow", "Sell"))
        self.salesResetAllButton.setText(_translate("SMSMainWindow", "Reset All"))
        self.salesPrintReceiptButton.setText(_translate("SMSMainWindow", "Print Receipt"))
        self.salesSearchDateEdit.setDisplayFormat(_translate("SMSMainWindow", "d/M/yyyy"))
        self.salesSearchParamComboBox.setItemText(0, _translate("SMSMainWindow", "Search By:"))
        self.salesSearchParamComboBox.setItemText(1, _translate("SMSMainWindow", "Item"))
        self.salesSearchParamComboBox.setItemText(2, _translate("SMSMainWindow", "Time(Hour)"))
        self.salesSearchParamComboBox.setItemText(3, _translate("SMSMainWindow", "Sales Person"))
        self.salesSearchField.setPlaceholderText(_translate("SMSMainWindow", "Type query here"))
        self.salesSearchButton.setText(_translate("SMSMainWindow", "Search"))
        self.salesSortLabel.setText(_translate("SMSMainWindow", "Sort By:"))
        self.salesSortComboBox.setItemText(0, _translate("SMSMainWindow", "Time"))
        self.salesSortComboBox.setItemText(1, _translate("SMSMainWindow", "Sales Person"))
        self.salesFlipTableButton.setText(_translate("SMSMainWindow", "Flip Table"))
        self.salesLoadTableButton.setText(_translate("SMSMainWindow", "Load Table"))
        self.salesPrevSearchButton.setText(_translate("SMSMainWindow", "Prev Search"))
        self.salesNextSearchButton.setText(_translate("SMSMainWindow", "Next Search"))
        item = self.salesRecordsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SMSMainWindow", "ITEM(S) SOLD"))
        item = self.salesRecordsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SMSMainWindow", "QUANTITY (COST)"))
        item = self.salesRecordsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SMSMainWindow", "TOTAL COST (GH₵)"))
        item = self.salesRecordsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SMSMainWindow", "DATE AND TIME"))
        item = self.salesRecordsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SMSMainWindow", "SALES PERSON"))
        self.label_7.setText(_translate("SMSMainWindow", "TOTAL SALES = GH₵"))
        self.todayNotifButton.setText(_translate("SMSMainWindow", "TODAY"))
        self.historyNotifButton.setText(_translate("SMSMainWindow", "HISTORY"))
        self.notifMsgLabel.setText(_translate("SMSMainWindow", "MESSAGES"))
        self.noNotifMsgLabel.setText(_translate("SMSMainWindow", "NO MESSAGES"))
        self.viewNotifTextEdit.setHtml(_translate("SMSMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.notifMsgViewLabel.setText(_translate("SMSMainWindow", "MESSAGE VIEW"))
        self.label_3.setText(_translate("SMSMainWindow", "DAILY SALES"))
        self.recordsDailyMonthComboBox.setItemText(0, _translate("SMSMainWindow", "Month"))
        self.recordsDailyMonthComboBox.setItemText(1, _translate("SMSMainWindow", "Jan"))
        self.recordsDailyMonthComboBox.setItemText(2, _translate("SMSMainWindow", "Feb"))
        self.recordsDailyMonthComboBox.setItemText(3, _translate("SMSMainWindow", "Mar"))
        self.recordsDailyMonthComboBox.setItemText(4, _translate("SMSMainWindow", "Apr"))
        self.recordsDailyMonthComboBox.setItemText(5, _translate("SMSMainWindow", "May"))
        self.recordsDailyMonthComboBox.setItemText(6, _translate("SMSMainWindow", "Jun"))
        self.recordsDailyMonthComboBox.setItemText(7, _translate("SMSMainWindow", "Jul"))
        self.recordsDailyMonthComboBox.setItemText(8, _translate("SMSMainWindow", "Aug"))
        self.recordsDailyMonthComboBox.setItemText(9, _translate("SMSMainWindow", "Sep"))
        self.recordsDailyMonthComboBox.setItemText(10, _translate("SMSMainWindow", "Oct"))
        self.recordsDailyMonthComboBox.setItemText(11, _translate("SMSMainWindow", "Nov"))
        self.recordsDailyMonthComboBox.setItemText(12, _translate("SMSMainWindow", "Dec"))
        self.dailyRecordsViewButton.setText(_translate("SMSMainWindow", "View"))
        self.label_4.setText(_translate("SMSMainWindow", "MONTHLY SALES"))
        self.monthlyRecordsViewButton.setText(_translate("SMSMainWindow", "View"))
        self.label_6.setText(_translate("SMSMainWindow", "ANNUAL SALES"))
        self.label_11.setText(_translate("SMSMainWindow", "From:"))
        self.label_10.setText(_translate("SMSMainWindow", "To:"))
        self.yearlyRecordsViewButton.setText(_translate("SMSMainWindow", "View"))
        self.recordsSearchDateEdit.setDisplayFormat(_translate("SMSMainWindow", "d/M/yyyy"))
        self.recordsSearchParamComboBox.setItemText(0, _translate("SMSMainWindow", "Search By:"))
        self.recordsSearchParamComboBox.setItemText(1, _translate("SMSMainWindow", "Item"))
        self.recordsSearchParamComboBox.setItemText(2, _translate("SMSMainWindow", "Time(Hour)"))
        self.recordsSearchParamComboBox.setItemText(3, _translate("SMSMainWindow", "Sales Person"))
        self.recordsSearchField.setPlaceholderText(_translate("SMSMainWindow", "Type query here"))
        self.recordsSearchButton.setText(_translate("SMSMainWindow", "Search"))
        self.recordsSortLabel.setText(_translate("SMSMainWindow", "Sort By:"))
        self.recordsSortComboBox.setItemText(0, _translate("SMSMainWindow", "Time"))
        self.recordsSortComboBox.setItemText(1, _translate("SMSMainWindow", "Sales Person"))
        self.recordsFlipTableButton.setText(_translate("SMSMainWindow", "Flip Table"))
        self.recordsLoadTableButton.setText(_translate("SMSMainWindow", "Load Table"))
        self.recordsPrevSearchButton.setText(_translate("SMSMainWindow", "Prev Search"))
        self.recordsNextSearchButton.setText(_translate("SMSMainWindow", "Next Search"))
        item = self.recordsTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SMSMainWindow", "ITEM(S) SOLD"))
        item = self.recordsTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SMSMainWindow", "QUANTITY (COST)"))
        item = self.recordsTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SMSMainWindow", "TOTAL COST (GH₵)"))
        item = self.recordsTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SMSMainWindow", "DATE AND TIME"))
        item = self.recordsTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SMSMainWindow", "SALES PERSON"))
        self.label_13.setText(_translate("SMSMainWindow", "TOTAL SALES = GH₵"))
        self.accountSettingsButton.setText(_translate("SMSMainWindow", "ACCOUNT"))
        self.stockSettingsButton.setText(_translate("SMSMainWindow", "STOCK"))
        self.otherSettingsButton.setText(_translate("SMSMainWindow", "OTHERS"))
        self.label_17.setText(_translate("SMSMainWindow", "EDIT SALES PERSON"))
        self.label_25.setText(_translate("SMSMainWindow", "Select Username:"))
        self.label_26.setText(_translate("SMSMainWindow", "Current Password:"))
        self.label_27.setText(_translate("SMSMainWindow", "New Username:"))
        self.editSalesPersonShowHideNewPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.label_28.setText(_translate("SMSMainWindow", "New Password:"))
        self.editSalesPersonShowHideConfirmPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.label_31.setText(_translate("SMSMainWindow", "Confirm Password:"))
        self.editSalesPerosnCancelButton.setText(_translate("SMSMainWindow", "Clear"))
        self.editSalesPersonSaveButton.setText(_translate("SMSMainWindow", "Save Changes"))
        self.editSalesPersonShowHideCurrentPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.label.setText(_translate("SMSMainWindow", "ADD SALES PERSON"))
        self.label_18.setText(_translate("SMSMainWindow", "Username: "))
        self.label_19.setText(_translate("SMSMainWindow", "Password: "))
        self.label_20.setText(_translate("SMSMainWindow", "Confirm Password:"))
        self.addSalesPersonClearButton.setText(_translate("SMSMainWindow", "Clear"))
        self.addSalesPersonSubmitButton.setText(_translate("SMSMainWindow", "Submit"))
        self.viewAllSalesPersonsButton.setText(_translate("SMSMainWindow", "All Personnel"))
        self.addSalesPersonShowHideConfirmPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.addSalesPersonHideShowPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.label_14.setText(_translate("SMSMainWindow", "REMOVE SALES PERSON"))
        self.label_21.setText(_translate("SMSMainWindow", "Select Username:"))
        self.removeSalesPersonRevokeButton.setText(_translate("SMSMainWindow", "Revoke"))
        self.removeSalesPersonConfirmButton.setText(_translate("SMSMainWindow", "Confirm"))
        self.label_22.setText(_translate("SMSMainWindow", "EDIT ADMINISTRATOR"))
        self.label_29.setText(_translate("SMSMainWindow", "Admin Name:"))
        self.editAdminNameLineEdit.setText(_translate("SMSMainWindow", "Admin"))
        self.label_30.setText(_translate("SMSMainWindow", "Current Password:"))
        self.label_32.setText(_translate("SMSMainWindow", "New Password:"))
        self.label_33.setText(_translate("SMSMainWindow", "Confirm Password:"))
        self.editAdminCancelButton.setText(_translate("SMSMainWindow", "Clear"))
        self.editAdminSaveButton.setText(_translate("SMSMainWindow", "Save Changes"))
        self.editAdminShowHideConfirmPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.editAdminShowHideNewPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.editAdminShowHideCurrentPasswordButton.setToolTip(_translate("SMSMainWindow", "Show Password"))
        self.label_40.setText(_translate("SMSMainWindow", "Description:"))
        self.label_41.setText(_translate("SMSMainWindow", "Unit Price:  "))
        self.label_51.setText(_translate("SMSMainWindow", " GH₵ "))
        self.label_42.setText(_translate("SMSMainWindow", "Quantity:"))
        self.addNewItemClearButton.setText(_translate("SMSMainWindow", "Clear"))
        self.addNewItemAddButton.setText(_translate("SMSMainWindow", "Add"))
        self.viewAllItemsButton.setText(_translate("SMSMainWindow", "All Items"))
        self.label_38.setText(_translate("SMSMainWindow", "ADD NEW ITEM"))
        self.label_43.setText(_translate("SMSMainWindow", "Choose Item:"))
        self.label_34.setText(_translate("SMSMainWindow", "Unit Price:  "))
        self.label_50.setText(_translate("SMSMainWindow", " GH₵"))
        self.label_44.setText(_translate("SMSMainWindow", "Quantity:"))
        self.removeItemClearButton.setText(_translate("SMSMainWindow", "Clear"))
        self.removeItemRemoveButton.setText(_translate("SMSMainWindow", "Remove"))
        self.label_36.setText(_translate("SMSMainWindow", "REMOVE ITEM"))
        self.label_35.setText(_translate("SMSMainWindow", "EDIT ITEM"))
        self.label_46.setText(_translate("SMSMainWindow", "Choose Item:"))
        self.label_47.setText(_translate("SMSMainWindow", "Current Quantity:"))
        self.label_48.setText(_translate("SMSMainWindow", "Current Unit Price: "))
        self.label_52.setText(_translate("SMSMainWindow", " GH₵ "))
        self.label_49.setText(_translate("SMSMainWindow", "Add Quantity:"))
        self.label_53.setText(_translate("SMSMainWindow", "New Unit Price:"))
        self.label_54.setText(_translate("SMSMainWindow", " GH₵ "))
        self.editItemClearButton.setText(_translate("SMSMainWindow", "Clear"))
        self.editItemUpdateButton.setText(_translate("SMSMainWindow", "Update"))
        self.label_56.setText(_translate("SMSMainWindow", "NOTIFICATION"))
        self.label_60.setText(_translate("SMSMainWindow", "Minimum Quantity of Items to Notify:"))
        self.saveNotifSettingsButton.setText(_translate("SMSMainWindow", "Save"))
        self.firmNameLabel.setText(_translate("SMSMainWindow", "Firm Name:"))
        self.firmContactLabel.setText(_translate("SMSMainWindow", "Firm Contact:"))
        self.firmAddressLabel.setText(_translate("SMSMainWindow", "Firm Address:"))
        self.clearFirmInfoButton.setText(_translate("SMSMainWindow", "Clear"))
        self.loadFirmInfoButton.setText(_translate("SMSMainWindow", "Load Info"))
        self.updateFirmInfoButton.setText(_translate("SMSMainWindow", "Update"))
        self.label_62.setText(_translate("SMSMainWindow", "EDIT FIRM\'S INFO"))
        self.label_58.setText(_translate("SMSMainWindow", "BACK UP DATA"))
        self.backupDataTurnOnOffAutoBackupCheckBox.setText(_translate("SMSMainWindow", "Turn On / Off Auto BackUp"))
        self.label_59.setText(_translate("SMSMainWindow", "Time Interval in minutes : "))
        self.saveBackupSettingsButton.setText(_translate("SMSMainWindow", "Save"))
        self.backupDataBackupNowButton.setText(_translate("SMSMainWindow", "Back Up Now"))
        self.label_63.setText(_translate("SMSMainWindow", "RESTORE DATA"))
        self.restoreDataButton.setText(_translate("SMSMainWindow", "Restore Data"))

