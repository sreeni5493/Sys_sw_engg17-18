# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SmartFridge.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import generate_banana

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SmartFridge(object):
    def setupUi(self, SmartFridge):
        SmartFridge.setObjectName(_fromUtf8("SmartFridge"))
        SmartFridge.resize(800, 600)
        self.centralwidget = QtGui.QWidget(SmartFridge)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridWidget = QtGui.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(20, 40, 761, 371))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.gridWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        
        self.toolButton_31 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_31.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_31.setFont(font)
        self.toolButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_31.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_31.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_31.setAutoRaise(True)
        self.toolButton_31.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_31.setObjectName(_fromUtf8("toolButton_31"))
        self.verticalLayout_9.addWidget(self.toolButton_31)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 150, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.gridWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.buttonBox = QtGui.QDialogButtonBox(self.gridWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Open)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox, QtCore.Qt.AlignLeft)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_16 = QtGui.QLabel(self.gridWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_7.addWidget(self.label_16)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.toolButton_3 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_3.setFont(font)
        self.toolButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_3.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.verticalLayout_4.addWidget(self.toolButton_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.gridWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.spinBox_1 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_1.setMaximum(9999)
        self.spinBox_1.setProperty("value", 1920)
        self.spinBox_1.setObjectName(_fromUtf8("spinBox_1"))
        self.horizontalLayout_8.addWidget(self.spinBox_1)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_8.addWidget(self.label_5)
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_2.setMaximum(9999)
        self.spinBox_2.setProperty("value", 1080)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.horizontalLayout_8.addWidget(self.spinBox_2)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.gridLayout.addWidget(self.groupBox_3, 5, 2, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.label = QtGui.QLabel(self.gridWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_12.addWidget(self.label)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.toolButton_10 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_10.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_10.setFont(font)
        self.toolButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_10.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_10.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_10.setObjectName(_fromUtf8("toolButton_10"))
        self.verticalLayout_11.addWidget(self.toolButton_10)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem8)
        self.horizontalLayout_12.addLayout(self.verticalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.gridWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_4.addWidget(self.checkBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout_4.addWidget(self.checkBox_3)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.gridLayout.addWidget(self.groupBox_4, 7, 2, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, 20, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.label_12 = QtGui.QLabel(self.gridWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_6.addWidget(self.label_12)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.toolButton_2 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.verticalLayout_3.addWidget(self.toolButton_2)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.spinBox_4 = QtGui.QSpinBox(self.gridWidget)
        self.spinBox_4.setProperty("value", 1)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 2, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.label_6 = QtGui.QLabel(self.gridWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.toolButton_5 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_5.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_5.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.verticalLayout_6.addWidget(self.toolButton_5)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem18)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_9, 6, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.gridWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem19, 0, 2, 1, 1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem20, 0, 3, 1, 1)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem21, 0, 4, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_2.addWidget(self.spinBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 6, 2, 1, 1)
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(20, 420, 761, 102))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalWidget)
        #self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem22)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem23 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem23)
        self.pushButton = QtGui.QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 0, 761, 31))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        self.label_2 = QtGui.QLabel(self.horizontalWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_13.addWidget(self.label_2)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem25)
        SmartFridge.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SmartFridge)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        SmartFridge.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SmartFridge)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SmartFridge.setStatusBar(self.statusbar)
        self.actionOpen_database_directory = QtGui.QAction(SmartFridge)
        self.actionOpen_database_directory.setObjectName(_fromUtf8("actionOpen_database_directory"))
        self.actionExit = QtGui.QAction(SmartFridge)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(SmartFridge)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_database_directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(SmartFridge)
        QtCore.QMetaObject.connectSlotsByName(SmartFridge)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generate_clicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_preview_clicked)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.open_std_directory)


    def retranslateUi(self, SmartFridge):
        #self.pushButton_2.hide()
        SmartFridge.setWindowTitle(_translate("SmartFridge", "SmartFridge", None))
        self.label_4.setText(_translate("SmartFridge", "Resolution", None))
        self.toolButton_31.setText(_translate("SmartFridge", "i", None))
        self.label_16.setText(_translate("SmartFridge", "Stages of decay  ", None))
        self.toolButton_3.setText(_translate("SmartFridge", "i", None))
        self.label_5.setText(_translate("SmartFridge", "x", None))
        self.label.setText(_translate("SmartFridge", "Path to the database", None))
        self.toolButton_10.setText(_translate("SmartFridge", "i", None))
        self.checkBox.setText(_translate("SmartFridge", "good", None))
        self.checkBox_2.setText(_translate("SmartFridge", "partially rotten", None))
        self.checkBox_3.setText(_translate("SmartFridge", "bad", None))
        self.label_12.setText(_translate("SmartFridge", "Number of images", None))
        self.toolButton_2.setText(_translate("SmartFridge", "i", None))
        self.label_6.setText(_translate("SmartFridge", "Number of fruits", None))
        self.toolButton_5.setText(_translate("SmartFridge", "i", None))
        self.pushButton_2.setText(_translate("SmartFridge", "Show preview", None))
        self.pushButton.setText(_translate("SmartFridge", "Generate", None))
        self.label_2.setText(_translate("SmartFridge", "SmartFridge", None))
        self.menuFile.setTitle(_translate("SmartFridge", "File", None))
        self.menuAbout.setTitle(_translate("SmartFridge", "About", None))
        self.actionOpen_database_directory.setText(_translate("SmartFridge", "Open database directory", None))
        self.actionExit.setText(_translate("SmartFridge", "Exit", None))
        self.actionAbout.setText(_translate("SmartFridge", "About", None))


        self.actionOpen_database_directory.triggered.connect(self.open_directory)
        self.actionExit.triggered.connect(self.close_application)
        self.actionAbout.triggered.connect(self.about_popup)



        self.spinBox_4.valueChanged.connect(self.sB4_value)
        self.spinBox_1.valueChanged.connect(self.sB1_value)
        self.spinBox_2.valueChanged.connect(self.sB2_value)
        self.spinBox.valueChanged.connect(self.sB0_value)

############# End Spinboxes

############# POPUPS

        self.toolButton_10.pressed.connect(self.info_popup_1)
        self.toolButton_31.pressed.connect(self.info_popup_2)
        #self.toolButton_6.pressed.connect(self.info_popup_3)

        self.toolButton_5.pressed.connect(self.info_popup_4)
        self.toolButton_3.pressed.connect(self.info_popup_5)
        self.toolButton_2.pressed.connect(self.info_popup_6)



    CB1 = 0
    CB2 = 1
    CB3 = 0

    lEd = '/'

    sB4 = 1              # number of images
    sB1 = 1920           # resolution X
    sB2 = 1080 
    sB0 = 1              # num pieces for image

    def sB4_value(self):
        self.sB4 = self.spinBox_4.value()
        print self.sB4 

    def sB1_value(self):
        self.sB1 = self.spinBox_1.value()
        print self.sB1

    def sB2_value(self):
        self.sB2 = self.spinBox_2.value()
        print self.sB2

    def sB0_value(self):
        self.sB0 = self.spinBox.value()
        print self.sB0 




    def CB1_checked(self):
        if self.checkBox.isChecked() == True:
            self.CB1 = 1
            print "CB1"
        else:
            self.CB1 = 0

    def CB2_checked(self):
        if self.checkBox_2.isChecked() == True:
            self.CB2 = 1
            print "CB2"
        else:
            self.CB2 = 0

    def CB3_checked(self):
        if se1f.checkBox_3.isChecked() == True:
            self.CB3 = 1
            print "CB3"
        else:
            self.CB3 = 0


    def open_std_directory(self):
        self.lEd = QtGui.QFileDialog.getExistingDirectory()
        print self.lEd
        self.lineEdit.setText(self.lEd)


    def open_directory(self):
        import os
        import platform
        import subprocess

        if platform.system() == "Windows" : 
            subprocess.Popen(['explorer', '/home/user'])
        elif platform.system() == 'Linux':
            subprocess.Popen(['xdg-open', self.lEd])
            
        #print dname
        #os.system()

    def close_application(self):
        import sys
        sys.exit()


    def about_popup(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'About','simulation tool version 0.4')


    def info_popup_1(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Path','Set standard path for the Sudoku directory.')

    def info_popup_2(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Resolution','Set resolution of the generated pictures.')

    def info_popup_3(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Difficulty','Easy - 0 , Medium -1, Hard -2, Insane - 3')
    
    def info_popup_4(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Various options','Errors in handwritten number: yes/no, \nMixed handwritten fonts: yes/no, \nSlightly view angle change: yes/no.')

    def info_popup_5(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Completion stages','Solved - handwritten and printed numbers occur, \nPartially solved - handwritten and printed numbers occur, empty cells, \nNot solved - printed numbers occur, emplty cells.')


    def info_popup_6(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Number of images','Number of images to generate')


    def info_popup_9(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Information','It might need some time, take a break.\nDirectory containing pictures will be opened.')


    def open_directory(self):
        import os
        import platform
        import subprocess

        if platform.system() == "Windows" : 
            subprocess.Popen(['explorer', '/home/user'])
        elif platform.system() == 'Linux':
            subprocess.Popen(['xdg-open', self.lEd])
    


    def generate_clicked(self):
        #s = sudoku_class.Sudoku("Hard",0,0)

        self.info_popup_9()
        
        b = generate_banana.call_banana_render(1,1,1)

        #if done == True:
        self.open_directory()



    def show_preview_clicked(self):
        
        print "show_preview has been activated"



def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    SmartFridge = QtGui.QMainWindow()
    ui = Ui_SmartFridge()
    ui.setupUi(SmartFridge)
    SmartFridge.show()
    sys.exit(app.exec_())


if __name__ == "__main__":    main()