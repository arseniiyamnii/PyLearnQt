##\file resultClass.py
##\brief class to result UI
#\details it file contain class, to view UI file with GUI \n to result window\n
##\warning it import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QProgressBar
from PyQt5.QtCore import QTimer
import time
##\brief class with result GUI
#\details same as file
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/result.ui",self)
        self.resultLabel=self.findChild(QLabel, "label")
        self.resultLabel.setText("hello world")
        self.timeBar=self.findChild(QProgressBar, "progressBar")
        self.timer = QTimer()
    ##\brief progress bar method
    #\details with running timer add to progress bar 10\n to value(like 10%)
    def handleTimer(self):
        value = self.timeBar.value()
        if value < 90:
            value = value + 10
            self.timeBar.setValue(value)
        else:
            self.timer.stop()
            self.close()
