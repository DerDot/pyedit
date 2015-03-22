#!/usr/bin/python

from PyQt4.QtGui import QApplication  # , QIcon
from src.PyEdit import PyEdit
import sys
# import os

def main():
    """
    A script to call the PyReader and execute it as a QApplication.
    """
    QApplication.setGraphicsSystem("raster")
    app = QApplication(sys.argv)
    app.setApplicationName('PyEdit')
    app.setOrganizationName("Me Corp.");
    # icon = QIcon(os.path.join("icons", "rss.ico"))
    # app.setWindowIcon(icon)
    # app.setQuitOnLastWindowClosed(False)
    wnd = PyEdit(sys.argv)
    # wnd.setWindowIcon(icon)
    wnd.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()
