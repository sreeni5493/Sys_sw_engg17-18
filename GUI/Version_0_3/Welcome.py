# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Welcome"))
        Form.resize(400, 202)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 381, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 381, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, _fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.toolButton_10 = QtGui.QToolButton(self.horizontalLayoutWidget)
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
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dialogButtonBox = KDialogButtonBox(Form)
        self.dialogButtonBox.setGeometry(QtCore.QRect(200, 150, 191, 34))
        self.dialogButtonBox.setAccessibleDescription(_fromUtf8(""))
        self.dialogButtonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.dialogButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.dialogButtonBox.setCenterButtons(False)
        self.dialogButtonBox.setObjectName(_fromUtf8("dialogButtonBox"))

        self.retranslateUi(Form)

        accd = QtCore.SIGNAL(_fromUtf8("accepted()"))
        #global rejd
        rejd = QtCore.SIGNAL(_fromUtf8("rejected()"))

        QtCore.QObject.connect(self.dialogButtonBox, accd, self.choose_simulation)
        QtCore.QObject.connect(self.dialogButtonBox, rejd, self.close_application)


        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Welcome", None))
        self.groupBox.setTitle(_translate("Form", "Welcome to simmulation tool, choose your task.", None))
        self.comboBox.setItemText(1, _translate("Form", "SudokuSolver", None))
        self.comboBox.setItemText(2, _translate("Form", "SmartFridge", None))
        self.toolButton_10.setText(_translate("Form", "?", None))
        self.toolButton_10.pressed.connect(self.info_popup)


    def choose_simulation(self):
        import SudokuSolver
        import SmartFridge

        text = self.comboBox.currentText()

        if (text == 'SudokuSolver'):
            SudokuS = QtGui.QMainWindow()
            ui = SudokuSolver.Ui_SudokuSolver()
            ui.setupUi(SudokuS)
            SudokuS.show()
            sys.exit(app.exec_())

        elif (text == 'SmartFridge'):
            #app = Ui_Form()
            SmartF = QtGui.QMainWindow()
            ui = SmartFridge.Ui_SmartFridge()
            ui.setupUi(SmartF)
            SmartF.show()
            sys.exit(app.exec_())







            #sys.exit()




    def close_application(self):
        sys.exit()


    def about_popup(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'About','simulation tool version 0.3')


    def info_popup(self):
        ppa = QtGui.QWidget()
        result = QtGui.QMessageBox.information(ppa,'Information','At the moment two tasks implemented \n simulations for SudokuSolver and SmartFridge.')







def main():    
        import sys
    #global app
        app = QtGui.QApplication(sys.argv)
        Form = QtGui.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())




from PyKDE4.kdeui import KDialogButtonBox

if __name__ == "__main__":
    main()
