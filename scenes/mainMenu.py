from Pyside6.QtWidgets import ( QWidget,
                                QLabel,
                                QPushButton,
                                QVBoxLayout,
                                QHBoxLayout)

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Mental Math Master"
        self.label = QLabel(self.title)
      
        self.startButton = QPushButton("Start")
      
        self.exitButton = QPushButton("Exit")
        self.exitButton.clicked.connect(self.exit)
      
        self.yesButton = QPushButton("Yes")
      
        self.noButton = QPushButton("No")
      
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

        self.vbox.addLayout(self.hbox)
        
        self.hbox.addWidget(self.yesButton)
        self.yesButton.hide()
      
        self.hbox.addWidget(self.noButton)
        self.noButton.hide()
    def exit(self):
        self.label.setText("Do you want to exit?")
        self.startButton.hide()
        self.exitButton.hide()
        self.yesButton.show()
        self.noButton.show()
    def no(self):
        pass
