# -*- coding: utf-8 -*-

"""
Module implementing Search.
"""
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from ui.Ui_Search import Ui_Search

class Search(QDialog, Ui_Search):
    """
    Class documentation goes here.
    """
    def __init__(self, textedit, correct):
        """
        Constructor
        """
        QDialog.__init__(self)
        self.setupUi(self)
        self.textedit = textedit
        
    @pyqtSignature("")
    def on_findButton_released(self):
        self.textedit._search(self.findEdit.text())
