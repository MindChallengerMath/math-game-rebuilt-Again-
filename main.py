from sceneChanger import SceneChanger
from gameSetup.operations import Operations
from scenes.mainMenu import MainMenu
import sys

if __name__ == "__main__":
  sceneChanger = SceneChanger()
  operations = Operations()
  mainMenu = MainMenu()
  sceneChanger.stack.addWidget(mainMenu)
  
