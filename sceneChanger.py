from PySide6.QtWidgets import (QStackedWidget)

class SceneChanger():
  def __init__(self):
    super().__init__()
    self.stack = QStackedWidget()
  def changeScene(self, scene):
    self.stack.currentIndex(scene)
    
