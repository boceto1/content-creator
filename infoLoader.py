from os.path import exists
from shutil import copyfile
from colorama import Fore
from utils import loadJsonFile, createJsonFile, toCamelCase

def createProjectFile(projectName, outDir):
  parsedProjectName = toCamelCase(projectName)

  print(Fore.BLUE + f'Creating Project File: {projectName}')
  templateProject = loadJsonFile('./templates/projectTemplate.json')
  templateProject['projectName'] = parsedProjectName
  createJsonFile(f'{outDir}/{parsedProjectName}.json', templateProject)
  print(Fore.GREEN + f'Project File created successfully: {projectName}')

def loadProjectFile(projectPath):
  if exists(projectPath):
    projectData = loadJsonFile(projectPath)
    return projectData
  else:
    raise Exception('File does not exists')
