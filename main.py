from moviepy.editor import *
from os.path import exists
from shutil import copyfile
from colorama import Fore


def createClips(baseVideo, clipTimes):
    clips = map(lambda clipTime: baseVideo.subclip(clipTime[0], clipTime[1]), clipTimes)
    return clips

def saveClips(clips):
  for index, clip in enumerate(clips):
    clip.write_videofile(f"test-clip{index}.mp4")

def clipsFileExists():
  if exists('./clips.csv'):
    return True
  print(Fore.RED + 'You are mising clips.csv file')
  print(Fore.BLUE + 'Creating clips.csv file...')
  copyfile('./templates/clips.csv', './clips.csv')
  print(Fore.YELLOW + 'Please, fill clips.csv file and run the program again')
  return False

def main():
   if (not clipsFileExists()):
      return

  #  baseVideo = VideoFileClip("test-video.mp4")
  #  clips = createClips(baseVideo, [[831, 950]])
  #  saveClips(clips)

main()




