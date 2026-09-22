from PySide6.QtWidgets import (QStackedWidget)

class SceneChanger():
  def __init__(self):
    super().__init__()
    self.stack = QStackedWidget()
    self.stack.setStyleSheet("""
    QStackedWidget{background-color: #231f1f;}""")
  def changeScene(self, scene):
    self.stack.setCurrentIndex(scene)