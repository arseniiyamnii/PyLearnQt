##\file settingsClass.py
##\brief SettingsWindow
#\details Create setting window using settings.ui file, and manage all Qt Widgets. It window add few settings, like Switch Language setting, and switch time to wait other exercise setting
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel,QComboBox, QSpinBox
import json
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
        with open("config.json", "rw") as configFile: #open config.json file, to read and write
            ##\brief config dictionary
            #\details dictionary, that load from config.json file,\n
            #witch contain information about language,\n
            #and time to waiting result window
            self.configDictionary=json.load(configFile) # create dictionary, from config.json file, with json module
