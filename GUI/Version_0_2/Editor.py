# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(791, 600)
        Form.setMinimumSize(QtCore.QSize(791, 600))
        Form.setMaximumSize(QtCore.QSize(792, 600))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 527, 771, 61))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.label_19 = QtGui.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 761, 41))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 521, 391))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(20, -1, 20, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(540, 350, 241, 131))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, -1, 20, 20)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 200, 241, 141))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 771, 61))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.verticalLayout.addWidget(self.pushButton_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Editor", None))
        self.pushButton_2.setText(_translate("Form", "Save", None))
        self.pushButton_2.clicked.connect(save_database)
        self.label_19.setText(_translate("Form", "                                                                      Database editor surely not necessary but nice to have.", None))
        self.pushButton_3.setText(_translate("Form", "<<", None))
        self.pushButton.setText(_translate("Form", ">>", None))
        self.pushButton_4.setText(_translate("Form", "Delete", None))
        self.pushButton_5.setText(_translate("Form", "Open", None))
        self.pushButton_5.clicked.connect(open_database)

def open_database(self):        
    fname = QtGui.QFileDialog.getOpenFileName()  
    
def save_database(self):
    sfname = QtGui.QFileDialog.getSaveFileName()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

