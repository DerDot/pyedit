from PyQt4.QtGui import QTextEdit, QMenu, QCompleter
from PyQt4.QtCore import pyqtSignature, pyqtSignal
from PyQt4.Qt import QSyntaxHighlighter, QAction, QTextCharFormat, Qt, QTextCursor

from src.BaseEdit import BaseEdit

import re

class SpellcheckEdit(QTextEdit, BaseEdit):
    
    def __init__(self, spell_dict):
        QTextEdit.__init__(self)
        BaseEdit.__init__(self)
        self.spell_dict = spell_dict
        self.highlighter = Highlighter(self.document(), self.spell_dict)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.customContextMenu)
        self.found = False
        self.edit_id = "spellcheck"
        self.completer = QCompleter(self.text())
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.setAcceptRichText(False)
        
    def text(self):
        return self.toPlainText()
        
    def set_dict(self, spell_dict):
        self.spell_dict = spell_dict
        self.highlighter = Highlighter(self.document(), self.spell_dict)
        
    def _search(self, search_string):
        if self.search_string != search_string:
            self.found = False
            self.search_string = search_string
        found = self.find(self.search_string)
        if not found and self.found:
            self._get_first(False)
            self._search(search_string)
        else:
            self.found = found
            
    def _get_first(self, select=True):
        cursor = self.textCursor()
        cursor.setPosition(0)
        self.setTextCursor(cursor)
        cursor.select(QTextCursor.WordUnderCursor)
        if select:
            self.setTextCursor(cursor)
        return cursor.selectedText()
            
    def _iterate(self):
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.WordRight)
        cursor.select(QTextCursor.WordUnderCursor)
        self.setTextCursor(cursor)
        return cursor.selectedText()
    
    def _replace(self, word):
        self.correctWord(word)
        
    @pyqtSignature("QPointF")
    def customContextMenu(self, point):
        popup_menu = self.createStandardContextMenu()
 
        # Select the word under the cursor.
        cursor = self.cursorForPosition(point)
        cursor.select(QTextCursor.WordUnderCursor)
        self.setTextCursor(cursor)
 
        # Check if the selected word is misspelled and offer spelling
        # suggestions if it is.
        if self.textCursor().hasSelection():
            text = unicode(self.textCursor().selectedText())
            if not self.spell_dict.check(text):
                spell_menu = QMenu('Spelling Suggestions')
                for word in self.spell_dict.suggest(text):
                    action = SpellAction(word, spell_menu)
                    action.correct.connect(self.correctWord)
                    spell_menu.addAction(action)
                # Only add the spelling suggests to the menu if there are
                # suggestions.
                if len(spell_menu.actions()) != 0:
                    popup_menu.insertSeparator(popup_menu.actions()[0])
                    popup_menu.insertMenu(popup_menu.actions()[0], spell_menu)
 
        popup_menu.exec_(self.mapToGlobal(point))
 
    def correctWord(self, word):
        '''
        Replaces the selected text with word.
        '''
        cursor = self.textCursor()
        cursor.beginEditBlock()
 
        cursor.removeSelectedText()
        cursor.insertText(word)
 
        cursor.endEditBlock()
        
        
class Highlighter(QSyntaxHighlighter):
 
    WORDS = u'(?iu)[\w\']+'
 
    def __init__(self, document, spell_dict):
        QSyntaxHighlighter.__init__(self, document)
        self.spell_dict = spell_dict
 
    def highlightBlock(self, text):
        text = unicode(text)
 
        tformat = QTextCharFormat()
        tformat.setUnderlineColor(Qt.red)
        tformat.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
 
        for word_object in re.finditer(self.WORDS, text):
            if not self.spell_dict.check(word_object.group()):
                self.setFormat(word_object.start(),
                    word_object.end() - word_object.start(), tformat)
                
class SpellAction(QAction):
 
    '''
    A special QAction that returns the text in a signal.
    '''
 
    correct = pyqtSignal(unicode)
 
    def __init__(self, *args):
        QAction.__init__(self, *args)
 
        self.triggered.connect(lambda x: self.correct.emit(
            unicode(self.text())))
