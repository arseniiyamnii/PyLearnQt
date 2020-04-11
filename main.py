#!/bin/env python3
##\file main.py
#\brief Main file witch running all program\n
#license MIT\n
##\warning dependence's:\n
#module \b os
from os import listdir
from os.path import isfile, join
import exerciseClass
import guiClass
from PyQt5.QtWidgets import QApplication
import sys
if __name__ == "__main__":
    ##\brief Array with path to all exercises
    excercises_path_list = [f for f in listdir("./exercises") if isfile(join("./exercises", f))]
    working_exercise=[]
    for one_exercise in excercises_path_list:
        working_exercise.append(exerciseClass.exercise("./exercises/"+one_exercise))
    app = QApplication(sys.argv)
    window = guiClass.UI(working_exercise)
    app.exec_()

