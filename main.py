from moviepy.editor import *
from os.path import exists
from shutil import copyfile
from colorama import Fore
import pandas as pd
from clipsCreator import createClips, saveClips, createReels

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

def main():
  if (not clipsFileExists()):
    return
  baseVideo = VideoFileClip("test-video.mp4")
  endVideo = VideoFileClip("./templates/endVideo.mp4")
  resizedVideo = baseVideo.resize((1080, 607.50))
  clipsData = getClipsData()
  clipsInfo = createClips(resizedVideo, clipsData)
  reelsInfo = createReels(clipsInfo, endVideo)
  saveClips(reelsInfo)

main()



# Next step: https://dev.to/ethand91/download-youtube-videos-with-python-4kp4
