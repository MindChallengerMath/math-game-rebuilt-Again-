from PySide6.QtWidgets import (QWidget,
                              QLabel,
                              QLineEdit,
                              QPushButton,
                              QVBoxLayout,
                              QHBoxLayout)
from PySide6.QtCore import Qt

class Game(QWidget):
    def __init__(self, operations):
        super().__init__()
        self.operations = operations
        self.score = 0
        self.answer = 0
        self.sign = ("+", "-", "*", "/")
        self.label = QLabel("Equation")
        self.userInput = QLineEdit()
        self.button = QPushButton("Enter")
        self.yesButton = QPushButton("Yes")
        self.noButton = QPushButton("No")
        self.initUI()
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.setStyleSheet("""
        """)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.hbox.addWidget(self.yesButton)
        self.yesButton.hide()
        self.hbox.addWidget(self.noButton)
        self.noButton.hide()