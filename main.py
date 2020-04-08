#!/bin/env python3
##\file main.py
#\brief Main file witch runing all program\n
#license MIT\n
##\warning dependensies:\n
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
    working_exercise=exerciseClass.exercise("./exercises/"+excercises_path_list[0])
    working_exercise.get_statements()
    working_exercise.create_vars()
    '''
    print(working_exercise.get_exercise_text())
    print(str(working_exercise.a)+" and "+str(working_exercise.b))
    print(working_exercise.compare_answer(input(": ")))
    '''
    app = QApplication(sys.argv)
    window = guiClass.UI(working_exercise)
    app.exec_()

