from PySide6.QtWidgets import (QWidget,
                              QLabel,
                              QLineEdit,
                              QPushButton,
                              QVBoxLayout,
                              QHBoxLayout)
from PySide6.QtCore import Qt
import random

class Game(QWidget):
    def __init__(self, operations):
        super().__init__()
        self.operations = operations
        self.maxNum = 10
        self.score = 0
        self.equation()
        self.label = QLabel(f"{self.n1} {self.sign} {self.n2}")
        self.userInput = QLineEdit()
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.enter)
        self.yesButton = QPushButton("Yes")
        self.noButton = QPushButton("No")
        self.initUI()
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.setStyleSheet("""
        """)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.errorLabel)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.hbox.addWidget(self.yesButton)
        self.yesButton.hide()
        self.hbox.addWidget(self.noButton)
        self.noButton.hide()
    def enter(self, value):
        try:
            value = float(self.userInput.text())
            if value == self.answer:
                self.score += 10
                self.equation()
            else:
                pass

        except ValueError:
            self.userInput.setText("This is not a number")
            
    def equation(self):
        self.n1 = random.randint(1, self.maxNum)
        self.n2 = random.randint(2, self.maxNum)
        self.sign = random.choice(("+", "-", "*", "/"))

        if self.sign == "+":
            self.answer = self.operations.plus(self.n1, self.n2)
        elif self.sign == "-":
            self.answer = self.operations.minus(self.n1, self.n2)
        elif self.sign == "*":
            self.answer = self.operations.multiply(self.n1, self.n2)
        else:
            self.answer = self.operations.divide(self.n1, self.n2)
        