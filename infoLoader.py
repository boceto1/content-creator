from os.path import exists
from shutil import copyfile
from colorama import Fore
import pandas as pd
from utils import loadJsonFile, createJsonFile, toCamelCase

def createProjectFile(projectName):
  parsedProjectName = toCamelCase(projectName)

  print(Fore.BLUE + f'Creating Project File: {projectName}')
  templateProject = loadJsonFile('./templates/projectTemplate.json')
  templateProject['projectName'] = parsedProjectName
  createJsonFile(f'./{parsedProjectName}.json', templateProject)
  print(Fore.GREEN + f'Project File created successfully: {projectName}')

def loadProjectFile(projectPath):
  if exists(projectPath):
    projectData = loadJsonFile(projectPath)
    return projectData
  else:
    raise Exception('File does not exists')

def clipsFileExists(clipsPath='./clips.csv'):
  if exists(clipsPath):
    return True
  print(Fore.RED + 'You are mising clips.csv file')
  print(Fore.BLUE + 'Creating clips.csv file...')
  copyfile('./templates/clips.csv', clipsPath)
  print(Fore.YELLOW + 'Please, fill clips.csv file and run the program again')
  return False

def getClipsData(clipsPath='./clips.csv'):
  clipsData = pd.read_csv(clipsPath)
  return clipsData.values
