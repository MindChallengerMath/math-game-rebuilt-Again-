from PySide6.QtWidgets import (QStackedWidget)

class SceneChanger():
  def __init__(self):
    super().__init__()
    self.stack = QStackedWidget()
    self.stack.setStyleSheet("""
    QStackedWidget{background-color: #231f1f;}
    QWidget{background-color: #2d2929; color: #0d8fec;
            font-family: "Times New Roman";}
    QPushButton{border-style: outset; border-width: 5px;
            border-color: #2a2928;}
            """)
  def changeScene(self, scene):
    self.stack.setCurrentIndex(scene)