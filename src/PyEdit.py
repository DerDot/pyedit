# -*- coding: utf-8 -*-

"""
Module implementing PyReader.
"""
from PyQt4.QtGui import QMainWindow, QFileDialog, QMessageBox
from PyQt4.QtCore import pyqtSignature
from PyQt4.Qsci import QsciLexerPython, QsciLexerCPP, QsciLexerBash, QsciLexerBatch, QsciLexerHTML, QsciLexerJava, QsciLexerJavaScript, QsciLexerTeX, QsciLexerFortran


from src.SpellcheckEdit import SpellcheckEdit
from src.SourceEdit import SourceEdit
from src.Search import Search
from src.SpellChecker import SpellChecker

import enchant
import codecs

import os

from ui.Ui_PyEdit import Ui_PyEdit

class PyEdit(QMainWindow, Ui_PyEdit):
    """
    Class documentation goes here.
    """
    def __init__(self, args):
        """
        Constructor
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.text = None
        self.path = ""
        self.lang_actions = {}
        for lang in enchant.list_languages():
            action = self.menuLanguages.addAction(lang)
            action.setCheckable(True)
            action.triggered.connect(self.on_languageChanged)
            self.lang_actions[lang] = action
        self.spell_dict = enchant.Dict()
        self.lang_actions[self.spell_dict.tag].setChecked(True)
        self.current_language = self.spell_dict.tag
        self.lexers = self.get_lexers()
        self.setChanged(False)
        self.search = None
        self.spell_checker = None
        if len(args) > 1:
            self.path = args[1]
            self.open()
        self.textEdit.textChanged.connect(self.on_textChanged)
            
    def open(self):
        ext = os.path.splitext(self.path)[1]
        lexer = None
        for extensions, alexer in self.lexers:
            if ext in extensions:
                lexer = alexer()
                break
        if lexer:
            self.changeEdit(SourceEdit(lexer))
        else:
            self.changeEdit(SpellcheckEdit(self.spell_dict))
        self.setWindowTitle("PyEdit - " + self.path)
        try:
            afile = codecs.open(self.path, "r", "utf-8")
            self.text = afile.read()
        except UnicodeDecodeError:
            afile.close()
            afile = codecs.open(self.path, "r", "latin9")
            self.text = afile.read()
        self.textEdit.setText(self.text)
        self.setChanged(False)
        self.textEdit.textChanged.connect(self.on_textChanged)
        
    def changeEdit(self, new_edit):
        self.textEdit.setParent(None)
        del(self.textEdit)
        self.textEdit = new_edit
        self.verticalLayout.addWidget(new_edit)
        
    def get_lexers(self):
        lexers = []
        lexers.append(([".py", ".pyw"], QsciLexerPython))
        lexers.append(([".c", ".cpp", ".h"], QsciLexerCPP))
        lexers.append(([".sh"], QsciLexerBash()))
        lexers.append(([".bat"], QsciLexerBatch()))
        lexers.append(([".html", ".htm"], QsciLexerHTML))
        lexers.append(([".java"], QsciLexerJava))
        lexers.append(([".js"], QsciLexerJavaScript))
        lexers.append(([".tex", ".latex", ".bibtex"], QsciLexerTeX))
        lexers.append(([".f90"], QsciLexerFortran))
        return lexers
    
    def setChanged(self, changed):
        self.changed = changed
        self.actionSave.setEnabled(changed)
        self.actionSave_as.setEnabled(changed)
    
    def closeEvent(self, event):
        if self.changed:
            warning = self.get_discard()
            res = warning.exec_()
            if res == QMessageBox.Save:
                self.on_actionSave_triggered()
            if res == QMessageBox.Cancel:
                event.ignore()
                return
        event.accept()
        
    @pyqtSignature("")
    def on_languageChanged(self):
        new_lang = str(self.sender().text())
        self.lang_actions[self.current_language].setChecked(False)
        self.current_language = new_lang
        self.spell_dict = enchant.Dict(new_lang)
        self.textEdit.set_dict(self.spell_dict)
        self.lang_actions[self.current_language].setChecked(True)
    
    @pyqtSignature("")
    def on_textChanged(self):
        self.setChanged(True)
        self.setWindowTitle("(*) " + self.path)
    
    @pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Calls the appropriate method if "Exit" in the menu is clicked.
        """
        self.close()
        
    @pyqtSignature("")
    def on_actionSearch_triggered(self):
        """
        Calls the appropriate method if "Search" in the menu is clicked.
        """
        self.search = Search(self.textEdit)
        self.search.exec_()
        
    @pyqtSignature("")
    def on_actionSave_triggered(self):
        """
        Calls the appropriate method if "Save" in the menu is clicked.
        """
        if self.changed:
            with open(self.path, "w") as outfile:
                outfile.write(self.textEdit.text())
            self.setChanged(False)
            self.setWindowTitle(self.path)
        
    @pyqtSignature("")
    def on_actionSave_as_triggered(self):
        """
        Calls the appropriate method if "Save as" in the menu is clicked.
        """
        if self.changed:
            path = QFileDialog.getSaveFileName(self, "Save document as", self.path)
            if path:
                self.path = str(path)
                self.on_actionSave_triggered()
                self.open()
            
    @pyqtSignature("")
    def on_actionOpen_triggered(self):
        """
        Calls the appropriate method if "Open" in the menu is clicked.
        """
        if self.changed:
            warning = self.get_discard()
            res = warning.exec_()
            if res == QMessageBox.Save:
                self.on_actionSave_triggered()
            if res == QMessageBox.Cancel:
                return
        path = QFileDialog.getOpenFileName(self, "Open document", self.path)
        if path:
            self.path = str(path)
            self.open()
            
    def get_discard(self):
        warning = QMessageBox()
        warning.setWindowTitle(self.path)
        warning.setText("The document has been modified.")
        warning.setInformativeText("Do you want to save your changes?")
        warning.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        warning.setDefaultButton(QMessageBox.Save)
        return warning

    @pyqtSignature("")
    def on_actionSpell_check_triggered(self):
        """
        Calls the appropriate method if "Spell check" in the menu is clicked.
        """
        self.spell_checker = SpellChecker(self.textEdit, self.spell_dict)
        self.spell_checker.exec_()
