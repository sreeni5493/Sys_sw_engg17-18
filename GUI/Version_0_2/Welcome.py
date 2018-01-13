# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import SmartFridge

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

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName(_fromUtf8("Welcome"))
        Welcome.setEnabled(True)
        Welcome.resize(401, 190)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Welcome.sizePolicy().hasHeightForWidth())
        Welcome.setSizePolicy(sizePolicy)
        Welcome.setMaximumSize(QtCore.QSize(401, 190))
        self.gridLayoutWidget = QtGui.QWidget(Welcome)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 381, 61))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 35))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Welcome)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 381, 61))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 35))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(Welcome)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 381, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)
        Welcome.setTabOrder(self.pushButton_2, self.pushButton)
        Welcome.setTabOrder(self.pushButton, self.pushButton_3)

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(_translate("Welcome", "Welcome", None))
        self.pushButton_2.setText(_translate("Welcome", "Generate vegatables", None))
        self.pushButton_2.clicked.connect(op_vege)
        self.pushButton.setText(_translate("Welcome", "Generate sudokus", None))
        self.pushButton.clicked.connect(op_sudo)
        self.pushButton_3.setText(_translate("Welcome", "Edit existing database", None))
        self.pushButton_3.clicked.connect(op_edit)
        self.label.setText(_translate("Welcome", "             Welcome to Simulation Tool v0.2 choose your task.", None))

def op_vege(self):
    import sys
    import SmartFridge
    Form = QtGui.QWidget()
    ui=SmartFridge.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
    
def op_sudo(self):
    import sys
    import Sudoku
    Form = QtGui.QWidget()
    ui=Sudoku.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


def op_edit(self):
    import sys
    import Editor
    Form = QtGui.QWidget()
    ui=Editor.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Welcome = QtGui.QWidget()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())

