from PyQt4.QtGui import QColor
from PyQt4.Qsci import QsciScintilla
from src.BaseEdit import BaseEdit

class SourceEdit(QsciScintilla, BaseEdit):
    
    def __init__(self, lexer):
        QsciScintilla.__init__(self)
        BaseEdit.__init__(self)
        self.setMarginWidth(0, 30)
        self.setMarginLineNumbers(0, True)
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#CCCCCC"))
        self.setBackspaceUnindents(True)
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionThreshold(1)
        self.setAutoCompletionCaseSensitivity(True)
        self.setTabIndents(True)
        self.setTabWidth(4)
        self.setLexer(lexer)
        self.edit_id = "source"
        
    def _search(self, search_string):
        self.search_string = search_string
        self.findFirst(self.search_string, False, False, False, True)
        
    def _get_first(self):
        self.findFirst("\w+", True, False, True, False, index=0)
        return self.selectedText()

    def _iterate(self):
        self.findFirst("\w+", True, False, True, False)
        return self.selectedText()
    
    def _replace(self, correction):
        self.replaceSelectedText(correction)
