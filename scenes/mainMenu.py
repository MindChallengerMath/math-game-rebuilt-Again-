from PySide6.QtWidgets import ( QWidget,
                                QLabel,
                                QPushButton,
                                QVBoxLayout,
                                QHBoxLayout)
from PySide6.QtCore import (Qt)
import sys
class MainMenu(QWidget):
    def __init__(self, sceneChanger):
        #Super makes the MainMenu class inherit the function and variables
        #from QWidgets
        super().__init__()
        self.sceneChanger = sceneChanger
        self.title = "Mental Math Master"
        self.label = QLabel(self.title)
      
        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.start)
      
        self.exitButton = QPushButton("Exit")
        self.exitButton.clicked.connect(self.exit)
      
        self.yesButton = QPushButton("Yes")
        self.yesButton.clicked.connect(self.yes)
      
        self.noButton = QPushButton("No")
        self.noButton.clicked.connect(self.no)
      
        self.initUI()
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
      
        self.setLayout(self.vbox)
        self.setStyleSheet("""
        """)
      
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.startButton)
        self.vbox.addWidget(self.exitButton)

        self.vbox.addLayout(self.hbox)
        
        self.hbox.addWidget(self.yesButton)
        self.yesButton.hide()
      
        self.hbox.addWidget(self.noButton)
        self.noButton.hide()
    def start(self):
        self.sceneChanger.changeScene(1)
    def exit(self):
        self.label.setText("Do you want to exit?")
        self.startButton.hide()
        self.exitButton.hide()
        self.yesButton.show()
        self.noButton.show()
    def yes(self):
        sys.exit()
    def no(self):
        self.label.setText(self.title)
        self.yesButton.hide()
        self.noButton.hide()
        self.startButton.show()
        self.exitButton.show()
