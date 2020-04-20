##\file settingsClass.py
##\brief SettingsWindow
#\details Create setting window using settings.ui file, and manage all Qt Widgets. It window add few settings, like Switch Language setting, and switch time to wait other exercise setting
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel,QComboBox, QSpinBox
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./qtUi/settings.ui", self)
        self.saveButton=self.findChild(QPushButton, "pushButton")
        self.saveExitButton=self.findChild(QPushButton, "pushButton_2")
        self.languageLabel=self.findChild(QLabel, "label")
        self.timelabel=self.findChild(QLabel, "label_2")
        self.languageCombo=self.findChild(QComboBox,"comboBox")
        self.timeSpin=self.findChild(QSpinBox, "spinBox")

