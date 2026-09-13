from Pyside6.QtWidgets import ( QWidget,
                                QLabel,
                                QPushButton,
                                QVBoxLayout,
                                QHBoxLayout)

class MainMenu(QWidget):
    def __init__(self):
        super().__init__(self)
        self.title = QLabel("Mental Math Master")
        self.startButton = QPushButton("Start")
        self.exitButton = QPushButton("Exit")
        self.initUI()
    def initUI(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setLayout(self.vbox)
        self.setStyleSheet("""
        """)
        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.startButton)
        self.vbox.addWidget(self.exitButton)
