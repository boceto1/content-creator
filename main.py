from clipsCreator import generateReels
from infoLoader import createProjectFile, loadProjectFile
import sys, getopt
from colorama import Fore
from GlobalStyles import GlobalStyles

def main():
  try:
    short_options = "c:g:"
    long_options = ["create", "generate"]
    args, _ = getopt.getopt(sys.argv[1:], short_options, long_options)

    for arg, value in args:
      if arg == "-c" or arg == "--create":
        createProjectFile(value)
        return
      elif arg == "-g" or arg == "--generate":
        projectData = loadProjectFile(value)    
        styles = projectData['styles'] if 'styles' in projectData else {}
        GlobalStyles.get_instance(styles)
        generateReels(projectData)
        return

  except Exception as e:
     print(Fore.RED + 'Error: This option is not valid: ' + str(e))

main()
