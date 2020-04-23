##\file settingsClass.py
##\brief SettingsWindow
#\details Create setting window using settings.ui file, and manage all Qt Widgets. It window add few settings, like Switch Language setting, and switch time to wait other exercise setting
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel,QComboBox, QSpinBox
import json
from os import listdir
from os.path import isfile, join
##\brief QT Window Settings
#\details Manage all widgets on Settings window,\n
#and using all functions
class UI(QMainWindow):
    ##\brief init all widgets
    #\details initialize all widgets drom settings.ui file,\n
    #and connect buttons to functions
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/settings.ui", self) #load settings.ui file with PYQt5.uic module (surprise)
        ##\brief Button to Save
        #\details initialise save button with QPushButton Widget
        self.saveButton=self.findChild(QPushButton, "pushButton")
        ##\brief Save and exit button
        #\details initialise Button to saving, and exit, with QPushButton Widget
        self.saveExitButton=self.findChild(QPushButton, "pushButton_2")
        ##\brief text about language
        #\details initiaise QLabel object, to show text about language
        self.languageLabel=self.findChild(QLabel, "label")
        ##\brief Time Text settings label
        #\details Initialise text field,\n
        # to view text, about time to waiting result window
        self.timelabel=self.findChild(QLabel, "label_2")
        ##\brief language combobox
        #\details initialise combobox, to show all avalible languages,\n
        # and chose one of them
        self.languageCombo=self.findChild(QComboBox,"comboBox")
        ##\brief time spin
        #\details initialise QSpinBox widget, to view anbd chose,\n
        #time to waiting result window
        self.timeSpin=self.findChild(QSpinBox, "spinBox")

        with open("config.json", "r") as configFile: #open config.json file, to read and write
            ##\brief config dictionary
            #\details dictionary, that load from config.json file,\n
            #witch contain information about language,\n
            #and time to waiting result window
            self.configDictionary=json.load(configFile) # create dictionary, from config.json file, with json module
        with open("./languages/"+self.configDictionary["language"]+".json","r") as langFile: #open language file
            ##\brief language dictionary
            #\details dictianary with language, from language file
            self.languageDictionary=json.load(langFile) #create dictionary from languageFile
        self.saveButton.clicked.connect(self.saveConfig) #connect function saveConfig to "Save" button
        self.saveExitButton.clicked.connect(self.saveConfigExit) #connect function saveConfigExit to "Save and Exit Button"
        self.timeSpin.setMinimum(1) #set minimum to spin box
        self.timeSpin.setMaximum(10) # set maximum to spin box
        self.timeSpin.setValue(int(self.configDictionary["tieWaitResult"])) # set current value to sin box (get it from config file)
        languages_path_list = [f for f in listdir("./languages") if isfile(join("./languages", f))] # get all languages pathes
        self.languageArray=[[],[]] #create clean array to languages pathes[0] and names[1]
        for language in languages_path_list: #appending items to previous array
            with open("./languages/"+language, "r") as langF:
                langDict=json.load(langF)

            self.languageArray[0].append(language[:-5])
            print(language[:-4])
            self.languageArray[1].append(langDict["language"])
        self.languageCombo.addItems(self.languageArray[1]) #adding items to language combobox
       #print(languageArray)
        self.languageCombo.setCurrentIndex(self.languageArray[0].index(self.configDictionary["language"])) #set current language, with finding current language in language array
    ##\brief Save Config
    #\details function to write new variables, to config.json file. 
    def saveConfig(self):
        ##\brief index new language
        #\details find index of new language in language array
        indexNewLanguage=self.languageArray[1].index(self.languageCombo.currentText())
        self.configDictionary["language"]=self.languageArray[0][indexNewLanguage]#change language entry in config Dictionary
        self.configDictionary["tieWaitResult"]=self.timeSpin.text()#change timeWaitResult in config dictionary
        with open("config.json", "w") as configFile: #open file to write changes
            json.dump(self.configDictionary, configFile) #write changes to file
    ##\brief Save and Exit
    #\details Function that run saveConfig function, for saving config, and then close window
    def saveConfigExit(self):
        self.saveConfig()
        self.close()
