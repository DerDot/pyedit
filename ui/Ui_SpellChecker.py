# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpellChecker.ui'
#
# Created: Mon Jun 17 19:02:06 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SpellChecker(object):
    def setupUi(self, SpellChecker):
        SpellChecker.setObjectName(_fromUtf8("SpellChecker"))
        SpellChecker.resize(530, 419)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(SpellChecker)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(SpellChecker)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.wordEdit = QtGui.QLineEdit(SpellChecker)
        self.wordEdit.setObjectName(_fromUtf8("wordEdit"))
        self.horizontalLayout.addWidget(self.wordEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.suggestList = QtGui.QListWidget(SpellChecker)
        self.suggestList.setObjectName(_fromUtf8("suggestList"))
        self.verticalLayout_2.addWidget(self.suggestList)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.correctButton = QtGui.QPushButton(SpellChecker)
        self.correctButton.setObjectName(_fromUtf8("correctButton"))
        self.verticalLayout.addWidget(self.correctButton)
        self.ignoreButton = QtGui.QPushButton(SpellChecker)
        self.ignoreButton.setObjectName(_fromUtf8("ignoreButton"))
        self.verticalLayout.addWidget(self.ignoreButton)
        self.ignoreAllButton = QtGui.QPushButton(SpellChecker)
        self.ignoreAllButton.setObjectName(_fromUtf8("ignoreAllButton"))
        self.verticalLayout.addWidget(self.ignoreAllButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SpellChecker)
        QtCore.QMetaObject.connectSlotsByName(SpellChecker)

    def retranslateUi(self, SpellChecker):
        SpellChecker.setWindowTitle(QtGui.QApplication.translate("SpellChecker", "Spell Checker", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SpellChecker", "Wrong word:", None, QtGui.QApplication.UnicodeUTF8))
        self.correctButton.setText(QtGui.QApplication.translate("SpellChecker", "Correct", None, QtGui.QApplication.UnicodeUTF8))
        self.ignoreButton.setText(QtGui.QApplication.translate("SpellChecker", "Ignore", None, QtGui.QApplication.UnicodeUTF8))
        self.ignoreAllButton.setText(QtGui.QApplication.translate("SpellChecker", "Ignore All", None, QtGui.QApplication.UnicodeUTF8))

