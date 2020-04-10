##/file resultClass.py
##\brief class to result UI
#\details it file contain class, to view UI file with GUI \n to result window\n
##\warning it import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
##\brief class with result GUI
#\details same as file
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/result.ui",self)
        ###
