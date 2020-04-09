from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/result.ui",self)
        ###
