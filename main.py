##\file main.py
#\brief Main file witch runing all program\n
#license MIT\n
##\warning dependensies:\n
#module \b os
from os import listdir
from os.path import isfile, join
import exerciseClass
if __name__ == "__main__":
    ##\brief Array with path to all exercises
    excercises_path_list = [f for f in listdir("./exercises") if isfile(join("./exercises", f))]
    a=exerciseClass.exercise("./exercises/"+excercises_path_list[0])
    a.get_statements()
    a.create_vars()
    print(a.get_exercise_text())
    print(str(a.a)+" and "+str(a.b))
    print(a.compare_answer(input(":")))
