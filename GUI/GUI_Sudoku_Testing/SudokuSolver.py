# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SudokuSolver.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sudoku_class

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

class Ui_SudokuSolver(object):
    def setupUi(self, SudokuSolver):
        SudokuSolver.setObjectName(_fromUtf8("SudokuSolver"))
        SudokuSolver.resize(800, 600)
        self.centralwidget = QtGui.QWidget(SudokuSolver)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridWidget = QtGui.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(20, 40, 761, 371))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.gridWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 7, 2, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.gridWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 5, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_2.addWidget(self.checkBox_3, 0, 4, 1, 1)
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_2.addWidget(self.checkBox_4, 0, 6, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 7, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 9, 2, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.label_15 = QtGui.QLabel(self.gridWidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_10.addWidget(self.label_15)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.toolButton_6 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_6.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_6.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_6.setObjectName(_fromUtf8("toolButton_6"))
        self.verticalLayout_7.addWidget(self.toolButton_6)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout_10, 7, 1, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.label_4 = QtGui.QLabel(self.gridWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_11.addWidget(self.label_4)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.toolButton_8 = QtGui.QToolButton(self.gridWidget)
        self.toolButton_8.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.toolButton_8.setFont(font)
        self.toolButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_8.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.toolButton_8.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolButton_8.setAutoRaise(True)
        self.toolButton_8.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_8.setObjectName(_fromUtf8("toolButton_8"))
        self.verticalLayout_9.addWidget(self.toolButton_8)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.gridLayout.addLayout(self.horizontalLayout_11, 5, 1, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
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
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem9)
        self.horizontalLayout_12.addLayout(self.verticalLayout_11)
        self.gridLayout.addLayout(self.horizontalLayout_12, 3, 1, 1, 1)
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
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.gridLayout.addWidget(self.groupBox_3, 5, 2, 1, 1)
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
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.buttonBox, QtCore.Qt.AlignLeft)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
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
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem14)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_9, 9, 1, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
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
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem16)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.gridWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout_4.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_8.setChecked(True)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.horizontalLayout_4.addWidget(self.radioButton_8)
        self.radioButton_9 = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.horizontalLayout_4.addWidget(self.radioButton_9)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.gridLayout.addWidget(self.groupBox_4, 8, 2, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, 20, -1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
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
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem19)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.spinBox_4 = QtGui.QSpinBox(self.gridWidget)
        self.spinBox_4.setProperty("value", 1)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem20)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 2, 1, 1)
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(20, 420, 761, 102))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem21)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem22 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem22)
        self.pushButton = QtGui.QPushButton(self.verticalWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 0, 761, 31))
        self.horizontalWidget.setObjectName(_fromUtf8("horizontalWidget"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem23)
        self.label_2 = QtGui.QLabel(self.horizontalWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_13.addWidget(self.label_2)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem24)
        SudokuSolver.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SudokuSolver)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        SudokuSolver.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SudokuSolver)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SudokuSolver.setStatusBar(self.statusbar)
        self.actionOpen_database_directory = QtGui.QAction(SudokuSolver)
        self.actionOpen_database_directory.setObjectName(_fromUtf8("actionOpen_database_directory"))
        self.actionExit = QtGui.QAction(SudokuSolver)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(SudokuSolver)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_database_directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(SudokuSolver)        

        QtCore.QMetaObject.connectSlotsByName(SudokuSolver)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.generate_clicked)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_preview_clicked)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.open_std_directory)



    def retranslateUi(self, SudokuSolver):
        self.pushButton_2.hide() # hide show preview 
        SudokuSolver.setWindowTitle(_translate("SudokuSolver", "Sudoku Solver", None))
        self.radioButton.setText(_translate("SudokuSolver", "0", None))
        self.radioButton_2.setText(_translate("SudokuSolver", "1", None))
        self.radioButton_3.setText(_translate("SudokuSolver", "2", None))
        self.radioButton_4.setText(_translate("SudokuSolver", "3", None))
        self.checkBox_3.setText(_translate("SudokuSolver", "Mixed fonts", None))
        self.checkBox_3.toggled.connect(self.CB3_checked)
        self.checkBox_4.setText(_translate("SudokuSolver", "Perspective variations", None))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.toggled.connect(self.CB4_checked)
        self.checkBox_2.setText(_translate("SudokuSolver", "Errors", None))
        self.checkBox_2.toggled.connect(self.CB2_checked)
        self.label_15.setText(_translate("SudokuSolver", "Difficulty  ", None))
        self.toolButton_6.setText(_translate("SudokuSolver", "i", None))
        self.label_4.setText(_translate("SudokuSolver", "Resolution", None))
        self.toolButton_8.setText(_translate("SudokuSolver", "i", None))
        self.label.setText(_translate("SudokuSolver", "Path for Sudokus", None))
        self.toolButton_10.setText(_translate("SudokuSolver", "i", None))
        self.label_5.setText(_translate("SudokuSolver", "x", None))
        self.label_6.setText(_translate("SudokuSolver", "Fine tunning", None))
        self.toolButton_5.setText(_translate("SudokuSolver", "i", None))
        self.label_16.setText(_translate("SudokuSolver", "Completion stage  ", None))
        self.toolButton_3.setText(_translate("SudokuSolver", "i", None))
        self.radioButton_7.setText(_translate("SudokuSolver", "solved", None))
        self.radioButton_8.setText(_translate("SudokuSolver", "partially solved", None))
        self.radioButton_9.setText(_translate("SudokuSolver", "not solved", None))
        self.label_12.setText(_translate("SudokuSolver", "Number of images", None))
        self.toolButton_2.setText(_translate("SudokuSolver", "i", None))        
        self.pushButton_2.setText(_translate("SudokuSolver", "Show preview", None))
        self.pushButton.setText(_translate("SudokuSolver", "Generate and Save", None))
        self.label_2.setText(_translate("SudokuSolver", "Sudoku Solver", None))
        self.menuFile.setTitle(_translate("SudokuSolver", "File", None))
        self.menuAbout.setTitle(_translate("SudokuSolver", "About", None))
        self.actionOpen_database_directory.setText(_translate("SudokuSolver", "Open Sudoku directory", None))
        self.actionExit.setText(_translate("SudokuSolver", "Exit", None))
        self.actionAbout.setText(_translate("SudokuSolver", "About", None))

        self.actionOpen_database_directory.triggered.connect(self.open_directory)
        self.actionExit.triggered.connect(self.close_application)
        self.actionAbout.triggered.connect(self.about_popup)



        self.spinBox_4.valueChanged.connect(self.sB4_value)
        self.spinBox_1.valueChanged.connect(self.sB1_value)
        self.spinBox_2.valueChanged.connect(self.sB2_value)

############# End Spinboxes

############# POPUPS

        self.toolButton_10.pressed.connect(self.info_popup_1)
        self.toolButton_8.pressed.connect(self.info_popup_2)
        self.toolButton_6.pressed.connect(self.info_popup_3)

        self.toolButton_5.pressed.connect(self.info_popup_4)
        self.toolButton_3.pressed.connect(self.info_popup_5)
        self.toolButton_2.pressed.connect(self.info_popup_6)
        
        #self.toolButton_11.pressed.connect(self.info_popup_7)
        #self.toolButton_13.pressed.connect(self.info_popup_8)
        #self.toolButton_14.pressed.connect(self.info_popup_9)       

############# End Popups       

############# Buttons

        self.radioButton.toggled.connect(self.rB1_toggled)
        self.radioButton_2.toggled.connect(self.rB2_toggled)
        self.radioButton_3.toggled.connect(self.rB3_toggled)
        self.radioButton_4.toggled.connect(self.rB4_toggled)
        #self.radioButton_5.toggled.connect(self.rB5_toggled)
        #self.radioButton_6.toggled.connect(self.rB6_toggled)
        self.radioButton_7.toggled.connect(self.rB7_toggled)
        self.radioButton_8.toggled.connect(self.rB8_toggled)
        self.radioButton_9.toggled.connect(self.rB9_toggled)
        
############# End Buttons


############# CheckBoxes

    CB2 = 0
    CB3 = 0
    CB4 = 1

    CB2CHK = False
    CB3CHK = False
    CB4CHK = False
############# End CheckBoxes



############# LineEdit 

    lEd = '/'  #std path

############## End LineEdit

############### SPIN BOXES Values

    sB4 = 1              # number of images
    sB1 = 1920           # resolution X
    sB2 = 1080           # resolution Y

############## End Spin Boxes


############### RADIO BUTTONS DEF and Variables   

    b1_stat = False # easy
    b2_stat = False # medium
    b3_stat = True  # hard
    b4_stat = False # insane
    #b5_stat = False
    #b6_stat = False
    b7_stat = False
    b8_stat = True
    b9_stat = False

    b1_count = 0 
    b2_count = 0 
    b3_count = 0 
    b4_count = 0 
    #b5_count = 0 
    #b6_count = 0 
    b7_count = 0 
    b8_count = 0 
    b9_count = 0

    dif = "Hard"
    cms = 1

    def sB4_value(self):
        self.sB4 = self.spinBox_4.value()
        print self.sB4 


    def sB1_value(self):
        self.sB1 = self.spinBox_1.value()

    def sB2_value(self):
        self.sB2 = self.spinBox_2.value()




    def rB1_toggled(self):
        print "b1"
        if self.b1_count % 2 == 0:
            self.b1_stat = True
        else:
            self.b1_stat = False

        self.b1_count += 1


    
    def rB2_toggled(self):
        print "b2"
        if self.b2_count % 2 == 0:
            self.b2_stat = True
        else:
            self.b2_stat = False

        self.b2_count += 1


    def CB2_checked(self):
        if self.checkBox_2.isChecked() == True:
            self.CB2 = 1
        else:
            self.CB2 = 0

    def CB3_checked(self):
        if self.checkBox_3.isChecked() == True:
            self.CB3 = 1
        else:
            self.CB3 = 0

    def CB4_checked(self):
        if self.checkBox_4.isChecked() == True:
            self.CB4 = 1
        else:
            self.CB4 = 0

    
    def rB3_toggled(self):
        print "b3"
        if self.b3_count % 2 == 0:
            self.b3_stat = True
        else:
            self.b3_stat = False

        self.b3_count += 1

    
    def rB4_toggled(self):
        print "b4"
        if self.b4_count % 2 == 0:
            self.b4_stat = True
        else:
            self.b4_stat = False

        self.b4_count += 1




    
    """ def rB5_toggled(self):
        print "b5"
        if self.b5_count % 2 == 0:
            self.b5_stat = True
        else:
            self.b5_stat = False

        self.b5_count += 1
       
    
    def rB6_toggled(self):
        print "b6"
        if self.b6_count % 2 == 0:
            self.b6_stat = True
        else:
            self.b6_stat = False

        self.b6_count += 1 """


    def rB7_toggled(self):
        print "b7"
        if self.b7_count % 2 == 0:
            self.b7_stat = True
        else:
            self.b7_stat = False

        self.b7_count += 1

    
    def rB8_toggled(self):
        print "b8"
        if self.b8_count % 2 == 0:
            self.b8_stat = True
        else:
            self.b8_stat = False

        self.b8_count += 1

    
    def rB9_toggled(self):
        print "b9"
        if self.b9_count % 2 == 0:
            self.b9_stat = True
        else:
            self.b9_stat = False

        self.b9_count += 1




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
        sys.exit()



################# POPUP MESSAGES DEF


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


    def info_popup_7(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Information','At the moment two tasks implemented \nsimulations for SudokuSolver and SmartFridge.')


    def info_popup_8(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Information','At the moment two tasks implemented \nsimulations for SudokuSolver and SmartFridge.')

    def info_popup_9(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Information','It might need some time, take a break.\nDirectory containing pictures will be opened.')

    def set_diff_str(self):
        if self.b1_stat == True: # easy
            self.dif = "Easy"
        elif self.b2_stat == True: # medium
            self.dif = "Medium"
        elif self.b3_stat == True:  # hard:
            self.dif = "Hard"
        elif self.b4_stat == True: # insane
            self.dif = "Insane"


    def set_compl_sta(self):
        if self.b7_stat == True: #
            self.cms = '2'
        elif self.b8_stat == True: #
            self.cms = '1'
        elif self.b9_stat == True:  # 
            self.cms = '0'

    def generate_clicked(self):
        #s = sudoku_class.Sudoku("Hard",0,0)
        self.set_diff_str()
        #print self.dif
        self.set_compl_sta()
        print self.cms
        print self.dif
        self.info_popup_9()
        
        s = sudoku_class.Sudoku(self.lEd, self.dif, self.CB2, self.cms ,self.sB1, self.sB2, 1 , self.sB4, self.CB4, self.CB3)
        s.create()
        
        if s.done == True:
            self.open_directory()
        #subprocess.call(['python','sudoku_class.py'])
        #sys.exit()


    def show_preview_clicked(self):
        
        #print "hallo" #(self.sB1_value())

        print(str(self.sB1) + ' ' + str(self.sB2) + ' ' + str(self.sB4) + ' | ' + self.lEd  + ' & ' + str(self.CB2) + ' ' + str(self.CB3) + ' ' + str(self.CB4))
        #sys.exit()


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    SudokuSolver = QtGui.QMainWindow()
    ui = Ui_SudokuSolver()
    ui.setupUi(SudokuSolver)
    SudokuSolver.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()