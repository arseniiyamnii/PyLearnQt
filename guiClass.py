##\file guiClass.py
#\author Arsenii Yamnii
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
##\brief class with gui
#\details It class contain all Qt Widgets for main window,\n
#and run other windows, like result, and config window
class UI(QMainWindow):
    ##\brief initialize ui file
    #\details initialize all GUI qwidgets, to control them,\n
    #connect functions to buttons,\n
    #set text to buttons from language dictionary,\n
    def __init__(self,working_exercise):
        with open("languages/language.json", "r") as language_file:
            ##\brief dictionary with language
            #\details contain dictionary with language. 
            self.language_dict = json.load(language_file)
        ##\brief exercise array
        #\details array that contain all exercise objects.\n
        self.working_exercise=working_exercise
        super(UI, self).__init__()
        uic.loadUi("./qtUi/main.ui", self)
        ##\brief exercise widget
        #\details that widget contain text with exercise,\n
        #and variables.
        self.exerciseText=self.findChild(QTextBrowser, "textBrowser")
        ##\brief answer winget
        #\details that widget for user input...answer input.
        self.answerLine=self.findChild(QLineEdit, "lineEdit")
        ##\brief Settings button
        #\details QT widget with TopMenu button 'Settings'
        self.menuSettingsButton=self.findChild(QAction, "actionSettings")
        ##\brief File button
        #\details TopMenu button 'File'
        self.menuFileButton=self.findChild(QMenu, "menuFile")

        self.menuFileButton.setTitle(self.language_dict["words"]["topMenuFile"])
        self.menuSettingsButton.setText(self.language_dict["words"]["topMenuSettings"])
        ##\brief push button widget
        #\details QT widget Button to Push Redy answer
        self.pushAnswerBtton=self.findChild(QPushButton,"pushButton")
        self.pushAnswerBtton.setText(self.language_dict["words"]["pushButton"])#add text to PushButton
        self.pushAnswerBtton.clicked.connect(self.getAnswerText)#here we add some function to pushbutton
        self.getExercise()
        self.addExerciseText()
        self.show()
    ##\brief function that add text with exercise
    def addExerciseText(self):
        self.exerciseText.setText("a="+str(self.runing_exercise.a)+"\nb="+str(self.runing_exercise.b)+"\n"+self.runing_exercise.get_exercise_text())
    ##\brief get answer text
    #\details Push answer text to runing_exercise.coomare_answer function,\n
    #get result from compare_answer in bool format,\n
    #send it to resultwindow function\n
    #,\n and remove text from input line
    def getAnswerText(self):
        self.resultWindow(self.runing_exercise.compare_answer(self.answerLine.text()))
        self.answerLine.setText("")
    ##\brief open result window
    def resultWindow(self,answer):
        ##\brief result window object
        #\details object that contain all result window Widgets
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
    ##\brief Switch exercise
    #\details Insert to runing_exercise variable, new obgect from working_exercise array
    def getExercise(self):
        self.runing_exercise=self.working_exercise[random.randint(0,len(self.working_exercise)-1)]
        self.runing_exercise.get_statements()
        self.runing_exercise.create_vars()
