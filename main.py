from moviepy.editor import *
from os.path import exists
from os import mkdir
from shutil import copyfile
from colorama import Fore
import pandas as pd
from re import sub

def toCamelCase(string):  
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")  
    return string[0].lower() + string[1:]  

def createClip(baseVideo, clipData):
  name,startTime,endTime = clipData
  clip = baseVideo.subclip(startTime, endTime)
  fileName = toCamelCase(name) + '.mp4'
  return [fileName, clip]

def createClips(baseVideo, clipsData):
    clips = map(lambda clipData: createClip(baseVideo, clipData), clipsData)
    return clips

def saveClips(clipsInfo):
  mkdir('./out')
  for index, clipInfo in enumerate(clipsInfo):
    fileName, clip = clipInfo
    print(Fore.BLUE + 'Creating ' + f"{index +1}_{fileName}")
    print(Fore.WHITE)
    clip.write_videofile(f"./out/{index +1}_{fileName}")
    print(Fore.GREEN + fileName + 'created successfully')

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
  clipsData = getClipsData()
  clipsInfo = createClips(baseVideo, clipsData)
  saveClips(clipsInfo)

main()
