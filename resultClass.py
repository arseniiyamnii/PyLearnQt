#\file resultClass.py
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
    ##\brief initialise UI
    #\details show UI from result.ui file, and run timer
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/result.ui",self) #load result ui file, and show it
        ##\brief QLabel for result text
        #\details 
        self.resultLabel=self.findChild(QLabel, "label")
        ##\brief QProgressBar for time
        #\details 
        self.timeBar=self.findChild(QProgressBar, "progressBar")
        ##\brief QTimer for QProgressBar
        #\details 
        self.timer = QTimer()
    ##\brief progress bar method
    #\details with running timer add to progress bar 10\n to value(like 10%)
    def handleTimer(self):
        value = self.timeBar.value()
        if value < 90: # first value its 0
            value = value + 30
            self.timeBar.setValue(value)
        else: #after 3 sec value being equal 90 (0+30+30+30)
            self.timer.stop() #stop timer
            self.close() #close result window
