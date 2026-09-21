from PySide6.QtWidgets import ( QWidget,
                                QLabel,
                                QPushButton,
                                QLineEdit,
                                QVBoxLayout)
from PySide6.QtCore import Qt

class DifficultyMenu(QWidget):
    def __init__(self, sceneChanger):
        super().__init__()
        self.sceneChanger = sceneChanger

        self.difficulty = 0
        self.label = QLabel("Enter desired difficulty(Interger)")

        self.userInput = QLineEdit()
        self.userInput.returnPressed.connect(self.enterDifficulty)

        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.enterDifficulty)

        self.initUI()
        
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.setStyleSheet("""
        """)

        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
    def enterDifficulty(self, value=0):
        try:
            value = int(self.userInput.text())
            if value > 0:
                self.difficulty = value
                self.userInput.clear()
                self.sceneChanger.changeScene(2)
            elif value == 0:
                self.label.setText("Zero is not a difficulty(Enter Difficulty)")
            else:
                self.label.setText("Input a positive number(Enter Difficulty)")
        except ValueError:
              self.label.setText("This is not an interger(Enter Difficulty)")