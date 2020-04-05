##\file guiClass.py
#\brief class with qt gui
#\warning dependensies\n
#module \b PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
import sys
##\brief class with gui
class UI(QMainWindow):
    ##\brief initialise ui file
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/main.ui", self)
        self.show()
