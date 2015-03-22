# -*- coding: utf-8 -*-

"""
Module implementing Search.
"""
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from ui.Ui_SpellChecker import Ui_SpellChecker

class SpellChecker(QDialog, Ui_SpellChecker):
    """
    Class documentation goes here.
    """
    def __init__(self, textedit, spell_dict):
        """
        Constructor
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.textedit = textedit
        self.spell_dict = spell_dict
        #self.wordEdit.textChanged.connect(self.on_wordEdit_textChanged)
        self.word = str(self.textedit._get_first()).strip("*?!+()/\\=:-.,#'\"")
        if self.word:
            self.fill()
        else:
            self.close()
        
    @pyqtSignature("")
    def on_correctButton_released(self):
        correction = self.wordEdit.text()
        self.textedit._replace(correction)
        self.iterate()
        
    @pyqtSignature("")
    def on_ignoreButton_released(self):
        self.iterate()
        
    @pyqtSignature("")
    def on_ignoreAllButton_released(self):
        self.spell_dict.add(self.word)
        self.iterate()
        
    @pyqtSignature("QString")
    def on_suggestList_currentTextChanged(self, text):
        self.wordEdit.setText(text)
            
    def iterate(self):
        self.suggestList.clear()
        self.word = str(self.textedit._iterate()).strip("*?!+()/\\=:-.,#'\"")
        if self.word:
            self.fill()
        else:
            self.close()
        
    def fill(self):
        if self.spell_dict.check(self.word):
            self.iterate()
        else:
            self.wordEdit.setText(self.word)
            for suggest in self.spell_dict.suggest(self.word):
                self.suggestList.addItem(suggest)
            self.suggestList.setCurrentRow(0)
