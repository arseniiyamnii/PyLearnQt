##\file exerciseClass.py
#\brief File with class for runing exercises
import random
##\brief Class for one exercise
class exercise():
    ##\brief init function
    #\details it get path to file,\n and create variable self.path
    def __init__(self,path):
        self.path=path
    ##\brief functon that return\n all statements for variable in exercise
    def get_statements(self):
        with open("./exercises/"+self.path) as file:
            ##\brief all lines in the fiile with exercise
            all_statement = file.readlines()
        ##\brief array with statements
        statement=[]
        statement.append(all_statement[1])
        statement.append(all_statement[2])
        for one_statement in statement:
            if one_statement[0]=="a":
                ##\brief Type of variable \a a
                self.a_type=one_statement[2:5]
                ##\brief mon for \a a variable
                self.a_range_from=one_statement[(one_statement.find("from")+5):(one_statement.find("to")-1)]
                ##\brief max for \a a variable
                self.a_range_to=one_statement[(one_statement.find("to")+3):-2]
            elif one_statement[0]=="b":
                ##\brief Type of variable \a b
                self.b_type=one_statement[2:5]
                ##\brief min for \a b variable
                self.b_range_from=one_statement[(one_statement.find("from")+5):(one_statement.find("to")-1)]
                ##\brief max for \a b variable
                self.b_range_to=one_statement[(one_statement.find("to")+3):-2]
    ##\brief function that create variables
    def create_vars(self):
        if self.a_type=="flo":
            ##\brief Created \a a variable
            self.a=random.uniform(float(self.a_range_from), float(self.a_range_to))
        else:
            ##\brief Created \a a variable
            self.a=random.randint(int(self.a_range_from),int(self.a_range_to))
        if self.b_type=="flo":
            ##\brief Created \a b variable
            self.b=random.uniform(float(self.b_range_from), float(self.b_range_to))
        else:
            ##\brief Created \a b variable
            self.b=random.randint(int(self.b_range_from),int(self.b_range_to))
    ##\brief function that compare answer
    #\warning this function can used only in python 3.3+(if i rigth)
    def compare_answer(self,answer):
        #it is for python 3.5+
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("module.name", self.path)
            ##\brief its not object. Its module with exercise
            self.program = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(self.program)
        #it is for python 3.3-3.4
        except:
            from importlib.machinery import SourceFileLoader
            self.program = SourceFileLoader("module.name", self.path).load_module()
        if (str(self.program.main(a,b))==str(answer)):
            return "true"
        else:
            return "false"
    def get_exercise_text(self):
        pass


