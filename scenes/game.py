from PySide6.QtWidgets import (QWidget,
                              QLabel,
                              QLineEdit,
                              QPushButton,
                              QVBoxLayout,
                              QHBoxLayout)
from PySide6.QtCore import Qt
import random

class Game(QWidget):
    def __init__(self, operations, difficultyMenu, sceneChanger):
        super().__init__()
        self.operations = operations
        self.difficultyMenu = difficultyMenu
        self.sceneChanger = sceneChanger

        self.defaultMaxNum = 10
        self.maxNum = self.defaultMaxNum

        self.score = 0

        self.createEquation()

        self.scoreLabel = QLabel(f"Score: {self.score}")
        self.label = QLabel(self.equation)

        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.enter)
        

        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.enter)

        self.restartButton = QPushButton("Restart")
        self.restartButton.clicked.connect(self.restart)

        self.mainMenuButton = QPushButton("Main Menu")
        self.mainMenuButton.clicked.connect(self.mainMenu)

        self.initUI()
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.setStyleSheet("""
        """)

        self.vbox.addWidget(self.scoreLabel)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)

        self.hbox = QHBoxLayout()

        self.vbox.addLayout(self.hbox)
        self.hbox.addWidget(self.restartButton)
        self.restartButton.hide()

        self.hbox.addWidget(self.mainMenuButton)
        self.mainMenuButton.hide()
    def enter(self, value=0):
        try:
            value = round(float(self.userInput.text()), 2)
            print(value)
            if value == self.answer:
                self.score += 10 + self.difficultyMenu.difficulty * 0.9
                self.maxNum += self.difficultyMenu.difficulty
                self.userInput.clear()
                print(self.maxNum)
                self.scoreLabel.setText(f"Score: {self.score}")

                self.createEquation()
                self.label.setText(self.equation)
            else:
                self.lose()

        except ValueError:
            self.userInput.setText("This is not a number")
    def lose(self):
        self.scoreLabel.setText("You Lose")
        self.label.setText(f"Final Score: {self.score}")

        self.userInput.clear()
        self.userInput.hide()

        self.button.hide()

        self.restartButton.show()
        self.mainMenuButton.show()

    def restart(self):
        self.score = 0

        self.maxNum = self.defaultMaxNum

        self.createEquation()

        self.scoreLabel.setText(f"Score: {self.score}")
        self.label.setText(self.equation)

        self.restartButton.hide()
        self.mainMenuButton.hide()

        self.userInput.show()

        self.button.show()
    def mainMenu(self):

        self.restart()
        
        self.sceneChanger.changeScene(0)
            
    def createEquation(self):
        self.n1 = random.randint(1, self.maxNum)
        self.n2 = random.randint(2, self.maxNum)

        self.sign = random.choice(("+", "-", "*", "/"))

        if self.sign == "+":
            self.answer = round(self.operations.plus(self.n1, self.n2), 2)
        elif self.sign == "-":
            self.answer = round(self.operations.minus(self.n1, self.n2), 2)
        elif self.sign == "*":
            self.answer = round(self.operations.multiply(self.n1, self.n2), 2)
        else:
            self.answer = round(self.operations.divide(self.n1, self.n2), 2)

        self.equation = f"{self.n1} {self.sign} {self.n2}"
        