from utils import toCamelCase
from os import mkdir
from colorama import Fore

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
