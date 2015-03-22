# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created: Mon Jun 10 13:08:51 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_Search(object):
    def setupUi(self, Search):
        Search.setObjectName(_fromUtf8("Search"))
        Search.setWindowModality(QtCore.Qt.ApplicationModal)
        Search.resize(509, 244)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Search.sizePolicy().hasHeightForWidth())
        Search.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Search)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Search)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.findEdit = QtGui.QLineEdit(Search)
        self.findEdit.setObjectName(_fromUtf8("findEdit"))
        self.gridLayout.addWidget(self.findEdit, 0, 1, 1, 1)
        self.findButton = QtGui.QPushButton(Search)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.gridLayout.addWidget(self.findButton, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Search)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.replaceEdit = QtGui.QLineEdit(Search)
        self.replaceEdit.setObjectName(_fromUtf8("replaceEdit"))
        self.gridLayout.addWidget(self.replaceEdit, 1, 1, 1, 1)
        self.replaceButton = QtGui.QPushButton(Search)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.gridLayout.addWidget(self.replaceButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtGui.QPushButton(Search)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Search)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("released()")), Search.reject)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        Search.setWindowTitle(_translate("Search", "Dialog", None))
        self.label.setText(_translate("Search", "Search:", None))
        self.findButton.setText(_translate("Search", "Find", None))
        self.label_2.setText(_translate("Search", "Replace with:", None))
        self.replaceButton.setText(_translate("Search", "Replace", None))
        self.cancelButton.setText(_translate("Search", "Cancel", None))

