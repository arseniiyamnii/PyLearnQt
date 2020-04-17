##\file guiClass.py
#\brief class with qt GUI
#\warning dependence's\n
#module \b PyQt5
from PyQt5 import uic
import random
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextBrowser, QLineEdit,QMenu,QAction
import sys
import resultClass
from PyQt5.QtCore import QTimer
import json
##\brief class with GUI
class UI(QMainWindow):
    ##\brief initialize ui file
    #\details initialize all GUI qwidgets, to control them\n
    #and connect functions to buttons
    def __init__(self,working_exercise):
        with open("language.json", "r") as language_file:
            self.language_dict = json.load(language_file)
        self.working_exercise=working_exercise
        super(UI, self).__init__()
        uic.loadUi("./qtUi/main.ui", self)
        ##\brief window with all exercise text
        self.exerciseText=self.findChild(QTextBrowser, "textBrowser")
        ##\brief line, with user answer
        self.answerLine=self.findChild(QLineEdit, "lineEdit")
        self.menuSettingsButton=self.findChild(QAction, "actionSettings")
        self.menuFileButton=self.findChild(QMenu, "menuFile")
        self.menuFileButton.setTitle(self.language_dict["words"]["topMenuFile"])
        self.menuSettingsButton.setText(self.language_dict["words"]["topMenuSettings"])
        self.pushAnswerBtton=self.findChild(QPushButton,"pushButton")
        self.pushAnswerBtton.setText(self.language_dict["words"]["pushButton"])
        self.pushAnswerBtton.clicked.connect(self.getAnswerText)#here we add some function to pushbutton
        ##Need to add init to Top Menu
        self.getExercise()
        self.addExerciseText()
        self.show()
    ##\brief function that add text with exercise
    def addExerciseText(self):
        self.exerciseText.setText("a="+str(self.runing_exercise.a)+"\nb="+str(self.runing_exercise.b)+"\n"+self.runing_exercise.get_exercise_text())
    ##\brief get answer text
    #\details print answer text to terminal,\n and remove text from input line
    def getAnswerText(self):
        self.resultWindow(self.runing_exercise.compare_answer(self.answerLine.text()))
        self.answerLine.setText("")
    ##\brief open result window
    def resultWindow(self,answer):
        self.dialog=resultClass.UI()
        if answer=="true":
            self.dialog.resultLabel.setText(self.language_dict["words"]["correct"])
        else:
            self.dialog.resultLabel.setText(self.language_dict["words"]["wrong"])
        self.dialog.show() 
        self.dialog.timer.timeout.connect(self.dialog.handleTimer)
        self.dialog.timer.start(1000)
        self.getExercise()
        #self.runing_exercise.change_exercise()
        self.runing_exercise.create_vars()
        self.addExerciseText()
    def getExercise(self):
        self.runing_exercise=self.working_exercise[random.randint(0,len(self.working_exercise)-1)]
        self.runing_exercise.get_statements()
        self.runing_exercise.create_vars()
