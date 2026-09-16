from sceneChanger import SceneChanger
from gameSetup.operations import Operations
from scenes.mainMenu import MainMenu
from scenes.difficultyMenu import DifficultyMenu
from PySide6 import (QApplication)
import sys

if __name__ == "__main__":
  app = QApplication()
  sceneChanger = SceneChanger()
  operations = Operations()
  mainMenu = MainMenu(sceneChanger)
  difficultyMenu = DifficultyMenu(sceneChanger)
  sceneChanger.stack.insertWidget(0, mainMenu)
  sceneChanger.stack.insertWidget(1, difficultyMenu)
  sceneChanger.stack.show()
  app.exec()
  
  
