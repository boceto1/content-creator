from utils import toCamelCase
from os import mkdir
from colorama import Fore
from moviepy.editor import *
from utils import addWordSpacing

def getFooterText():
  footerText = addWordSpacing('Experiences 404', 6)
  textClip = TextClip(footerText, font ="resources/BebasNeue-Regular.ttf", fontsize = 47.5, color ="#fbbc09")
  textClip = textClip.set_position(("center","bottom"))
  return textClip

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

def createReel(clipInfo, endVideo):
  fileName, clip = clipInfo
  clipDuration = clip.duration

  colorClip = ColorClip(size =(1080, 1920), color =[30, 30, 30], duration=clipDuration)
  footerText = getFooterText().set_duration(clipDuration)
  endVideo = VideoFileClip('./templates/endVideo.mp4')

  reel = CompositeVideoClip([colorClip.set_start(0),
                            clip.set_position(("center","center")).set_start(0),
                            footerText.set_start(0),
                            endVideo.set_start(clipDuration).crossfadein(1.5)])
  
  return [fileName, reel]

def createReels(clipsInfo, endVideo):
  return map(lambda clipInfo: createReel(clipInfo, endVideo), clipsInfo)
