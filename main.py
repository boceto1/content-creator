from moviepy.editor import *
from clipsCreator import createClips, saveClips, createReels
from infoLoader import clipsFileExists, getClipsData
from constants import VIDEO_DIMENSION
import sys, getopt
from colorama import Fore

def generateReels():
  if (not clipsFileExists()):
    return
  baseVideo = VideoFileClip("test-video.mp4")
  endVideo = VideoFileClip("./templates/endVideo.mp4")
  resizedVideo = baseVideo.resize((VIDEO_DIMENSION[0], VIDEO_DIMENSION[1]))
  clipsData = getClipsData()
  clipsInfo = createClips(resizedVideo, clipsData)
  reelsInfo = createReels(clipsInfo, endVideo)
  saveClips(reelsInfo)

def main():
  try:
    short_options = "c:g:"
    long_options = ["create", "generate"]
    args, _ = getopt.getopt(sys.argv[1:], short_options, long_options)

    for arg, value in args:
      if arg == "-c" or arg == "--create":
          # Handle create option
          print("Create option specified")
      elif arg == "-g" or arg == "--generate":
        # Handle generate option
        print("Generate option specified with value:", value)

  except Exception as e:
     print(Fore.RED + 'Error: This option is not valid: ' + str(e))

main()
