##/file resultClass.py
##\brief class to result UI
#\details it file contain class, to view UI file with GUI \n to result window\n
##\warning it import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QProgressBar
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
        #self.runTimer()
    def runTimer(self):
        self.timeBar.setMaximum(10)
        timeToExpired=0
        while timeToExpired<3:
            timeToExpired+=1
            time.sleep(1)
            self.timeBar.setValue(timeToExpired)
