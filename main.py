import sys
from sceneChanger import SceneChanger
from operations import Operations
from scenes.mainMenu import MainMenu
from scenes.difficultyMenu import DifficultyMenu
from scenes.game import Game
from PySide6.QtWidgets import (QApplication)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  sceneChanger = SceneChanger()
  operations = Operations()
  mainMenu = MainMenu(sceneChanger)
  difficultyMenu = DifficultyMenu(sceneChanger)
  game = Game(operations, difficultyMenu, sceneChanger)
  #This puts the widgets into the index
  sceneChanger.stack.insertWidget(0, mainMenu)
  sceneChanger.stack.insertWidget(1, difficultyMenu)
  sceneChanger.stack.insertWidget(2, game)
  sceneChanger.stack.show()
  sys.exit(app.exec())