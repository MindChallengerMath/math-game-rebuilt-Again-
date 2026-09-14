from sceneChanger import SceneChanger
from gameSetup.operations import Operations
from scenes.mainMenu import MainMenu
from PySide6 import (QApplication)
import sys

if __name__ == "__main__":
  app = QApplication()
  sceneChanger = SceneChanger()
  operations = Operations()
  mainMenu = MainMenu()
  sceneChanger.stack.insertWidget(mainMenu)
  sceneChanger.stack.show()
  app.exec()
  
  
