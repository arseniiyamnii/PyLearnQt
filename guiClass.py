##\file guiClass.py
#\brief class with qt gui
#\warning dependensies\n
#module \b PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextBrowser, QLineEdit
import sys
##\brief class with gui
class UI(QMainWindow):
    ##\brief initialise ui file
    #\details initialise all gui widgets, to control them\n
    #and coonnect functions to buttons
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/main.ui", self)
        ##\brief window with all exercise text
        self.exerciseText=self.findChild(QTextBrowser, "textBrowser")
        ##\brief line, with user answer
        self.answerLine=self.findChild(QLineEdit, "lineEdit")
        ##\brief button, to push answer
        self.pushAnswerBtton=self.findChild(QPushButton,"pushButton")
        self.pushAnswerBtton.clicked.connect(self.addExerciseText)
        self.show()
    ##\brief function that add text with exercise
    def addExerciseText(self):
        self.exerciseText.setText("fuuuuckyeeeah")

