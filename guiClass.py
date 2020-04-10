##\file guiClass.py
#\brief class with qt GUI
#\warning dependence's\n
#module \b PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextBrowser, QLineEdit
import sys
import resultClass
from PyQt5.QtCore import QTimer
##\brief class with GUI
class UI(QMainWindow):
    ##\brief initialize ui file
    #\details initialize all GUI qwidgets, to control them\n
    #and connect functions to buttons
    def __init__(self,working_exercise):
        self.working_exercise=working_exercise
        super(UI, self).__init__()
        uic.loadUi("./qtUi/main.ui", self)
        ##\brief window with all exercise text
        self.exerciseText=self.findChild(QTextBrowser, "textBrowser")
        ##\brief line, with user answer
        self.answerLine=self.findChild(QLineEdit, "lineEdit")
        ##\brief button, to push answer
        self.pushAnswerBtton=self.findChild(QPushButton,"pushButton")
        self.pushAnswerBtton.clicked.connect(self.getAnswerText)#here we add some function to pushbutton
        self.addExerciseText()
        self.show()
    ##\brief function that add text with exercise
    def addExerciseText(self):
        self.exerciseText.setText("a="+str(self.working_exercise.a)+"\nb="+str(self.working_exercise.b)+"\n"+self.working_exercise.get_exercise_text())
    ##\brief get answer text
    #\details print answer text to terminal,\n and remove text from input line
    def getAnswerText(self):
        self.resultWindow(self.working_exercise.compare_answer(self.answerLine.text()))
        self.answerLine.setText("")
    ##\brief open result window
    def resultWindow(self,answer):
        self.dialog=resultClass.UI()
        if answer=="true":
            self.dialog.resultLabel.setText("Correct")
        else:
            self.dialog.resultLabel.setText("Wrong!")
        self.dialog.show() 
        self.dialog.timer.timeout.connect(self.dialog.handleTimer)
        self.dialog.timer.start(1000)
        self.working_exercise.change_exercise()
        self.addExerciseText()
