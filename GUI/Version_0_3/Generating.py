# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Generating.ui'
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

class Ui_Generating(object):
    def setupUi(self, Generating):
        Generating.setObjectName(_fromUtf8("Generating"))
        Generating.resize(400, 189)
        self.verticalLayoutWidget = QtGui.QWidget(Generating)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 60, 381, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, -1, 20, 20)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.progressBar = QtGui.QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setProperty("value", 67)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Generating)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 381, 51))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayoutWidget = QtGui.QWidget(Generating)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 110, 381, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(self.horizontalLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Generating)
        QtCore.QMetaObject.connectSlotsByName(Generating)

    def retranslateUi(self, Generating):
        Generating.setWindowTitle(_translate("Generating", "Generating", None))
        self.label.setText(_translate("Generating", "                                        Generating please wait ..", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Generating = QtGui.QWidget()
    ui = Ui_Generating()
    ui.setupUi(Generating)
    Generating.show()
    sys.exit(app.exec_())

