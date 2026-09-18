from PySide6.QtWidget import (QWidget,
                              QLabel,
                              QLineEdit,
                              QPushButton,
                              QVBoxLayout,
                              QHBoxLayout)
from PySide6.QtCore import Qt

class Game(QWidget):
    def __init__(self, operations):
        self.operations = operations
        self.score = 0
        self.answer = 0
        self.sign = ("+", "-", "*", "/")
        self.label = QLabel("Equation")
        self.userInput = QLineEdit()
        self.button = QPushButton("Enter")
        self.yesButton = QPushButton("Yes")
        self.noButton = QPushButton("No")
        
