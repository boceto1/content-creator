from clipsCreator import generateReels
from infoLoader import createProjectFile, loadProjectFile
import sys, getopt
from colorama import Fore
from GlobalStyles import GlobalStyles

def main():
  try:
    short_options = "c:g:p:"
    long_options = ["create", "generate", "preview"]
    args, extraValues = getopt.getopt(sys.argv[1:], short_options, long_options)

    for arg, value in args:
      if arg == "-c" or arg == "--create":
        outDir = extraValues[0] if len(extraValues) == 1 else '.'
        createProjectFile(value, outDir)
        return
      elif arg == "-g" or arg == "--generate" or arg == "-p" or arg == "--preview":
        projectData = loadProjectFile(value)    
        styles = projectData['styles'] if 'styles' in projectData else {}
        GlobalStyles.get_instance(styles)
        isPreview = arg == "-p" or arg == "--preview" 
        generateReels(projectData, isPreview)
        return

  except Exception as e:
     print(Fore.RED + 'Error: This option is not valid: ' + str(e))

main()
