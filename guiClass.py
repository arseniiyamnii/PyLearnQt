##\file guiClass.py
#\brief class with qt gui
#\warning dependensies\n
#module \b PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTextBrowser, QLineEdit
import sys
import resultClass
##\brief class with gui
class UI(QMainWindow):
    ##\brief initialise ui file
    #\details initialise all gui qwidgets, to control them\n
    #and coonnect functions to buttons
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
        self.pushAnswerBtton.clicked.connect(self.resultWindow)#here we add some function to pushbutton
        self.dialog=resultClass.UI()
        self.show()
    ##\brief function that add text with exercise
    def addExerciseText(self):
        self.exerciseText.setText("a="+str(self.working_exercise.a)+"\nb="+str(self.working_exercise.b)+"\n"+self.working_exercise.get_exercise_text())

    def getAnswerText(self):
        print(self.answerLine.text())
        self.answerLine.setText("")
    def resultWindow(self):
        #resultApp=QApplication(sys.argv)
        self.dialog.show() 
