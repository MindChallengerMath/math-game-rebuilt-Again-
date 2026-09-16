from PySide6.QtWidgets import ( QWidget,
                                QLabel,
                                QPushButton,
                                QLineEdit,
                                QVBoxLayout)
from PySide6.QtCore import Qt

class difficultyMenu(QWidget):
    def __init__(self):
        super().__init__(self)
        label = QLabel("Enter desired difficulty(Interger)")
        userInput = QLineEdit()
        button = QPushButton("Enter")
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.setStyleSheet("""
        """)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.userInput)
        self.vbox.addWidget(self.button)
