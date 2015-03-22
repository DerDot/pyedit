# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyEdit.ui'
#
# Created: Mon Jun 10 13:08:54 2013
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

class Ui_PyEdit(object):
    def setupUi(self, PyEdit):
        PyEdit.setObjectName(_fromUtf8("PyEdit"))
        PyEdit.resize(800, 600)
        PyEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(PyEdit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        PyEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuLanguages = QtGui.QMenu(self.menubar)
        self.menuLanguages.setObjectName(_fromUtf8("menuLanguages"))
        PyEdit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyEdit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyEdit.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(PyEdit)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionZoom_in = QtGui.QAction(PyEdit)
        self.actionZoom_in.setObjectName(_fromUtf8("actionZoom_in"))
        self.actionZoom_out = QtGui.QAction(PyEdit)
        self.actionZoom_out.setObjectName(_fromUtf8("actionZoom_out"))
        self.actionSave = QtGui.QAction(PyEdit)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(PyEdit)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionOpen = QtGui.QAction(PyEdit)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSpell_check = QtGui.QAction(PyEdit)
        self.actionSpell_check.setObjectName(_fromUtf8("actionSpell_check"))
        self.actionSearch = QtGui.QAction(PyEdit)
        self.actionSearch.setObjectName(_fromUtf8("actionSearch"))
        self.actionH = QtGui.QAction(PyEdit)
        self.actionH.setObjectName(_fromUtf8("actionH"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSpell_check)
        self.menuTools.addAction(self.actionSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuLanguages.menuAction())

        self.retranslateUi(PyEdit)
        QtCore.QMetaObject.connectSlotsByName(PyEdit)

    def retranslateUi(self, PyEdit):
        PyEdit.setWindowTitle(_translate("PyEdit", "PyEdit", None))
        self.menuFile.setTitle(_translate("PyEdit", "File", None))
        self.menuTools.setTitle(_translate("PyEdit", "Tools", None))
        self.menuLanguages.setTitle(_translate("PyEdit", "Languages", None))
        self.actionExit.setText(_translate("PyEdit", "Exit", None))
        self.actionExit.setShortcut(_translate("PyEdit", "Ctrl+Q", None))
        self.actionZoom_in.setText(_translate("PyEdit", "Zoom in", None))
        self.actionZoom_in.setShortcut(_translate("PyEdit", "Ctrl+]", None))
        self.actionZoom_out.setText(_translate("PyEdit", "Zoom out", None))
        self.actionZoom_out.setShortcut(_translate("PyEdit", "Ctrl+-", None))
        self.actionSave.setText(_translate("PyEdit", "Save", None))
        self.actionSave.setShortcut(_translate("PyEdit", "Ctrl+S", None))
        self.actionSave_as.setText(_translate("PyEdit", "Save as", None))
        self.actionSave_as.setShortcut(_translate("PyEdit", "Ctrl+Shift+S", None))
        self.actionOpen.setText(_translate("PyEdit", "Open", None))
        self.actionOpen.setShortcut(_translate("PyEdit", "Ctrl+O", None))
        self.actionSpell_check.setText(_translate("PyEdit", "Spell check", None))
        self.actionSearch.setText(_translate("PyEdit", "Search", None))
        self.actionSearch.setShortcut(_translate("PyEdit", "Ctrl+F", None))
        self.actionH.setText(_translate("PyEdit", "h", None))

