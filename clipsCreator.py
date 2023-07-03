from utils import toCamelCase, createOutDir
from colorama import Fore
from moviepy.editor import *
from constants import FOOTER_TEXT, REELS_DIMENSION, MOCK_CLIP, getTopText, getBottomText

def createClip(baseVideo, clipData):
  name,startTime,endTime = clipData
  clip = baseVideo.subclip(startTime, endTime)
  fileName = toCamelCase(name) + '.mp4'
  return [fileName, clip]

def createClips(baseVideo, clipsData):
    clips = map(lambda clipData: createClip(baseVideo, clipData), clipsData)
    return clips

def createReel(clipInfo, endVideo):
  fileName, clip = clipInfo
  # clipDuration = clip.duration
  clipDuration = 2

  baseVideoShape = ColorClip(size =(REELS_DIMENSION[0], REELS_DIMENSION[1]), color =[30, 30, 30], duration=clipDuration)

  footerText = FOOTER_TEXT.set_duration(clipDuration)
  topText = getTopText('Aprende a diferenciar los recursos que consumes').set_duration(clipDuration)
  bottomText = getBottomText('según tu nivel de conocimiento o experiencia').set_duration(clipDuration)

  endVideo = VideoFileClip('./templates/endVideo.mp4')

  reel = CompositeVideoClip([
    baseVideoShape.set_start(0),
    MOCK_CLIP.set_duration(clipDuration).set_position(("center","center")).set_start(0),
    # clip.set_position(("center","center")).set_start(0),
    footerText.set_start(0),
    topText.set_start(0),
    bottomText.set_start(0),
    # endVideo.set_start(clipDuration).crossfadein(1.5)
  ])
  
  return [fileName, reel]

def createReels(clipsInfo, endVideo):
  return map(lambda clipInfo: createReel(clipInfo, endVideo), clipsInfo)

def saveClips(clipsInfo):
  createOutDir()
  for index, clipInfo in enumerate(clipsInfo):
    fileName, clip = clipInfo
    print(Fore.BLUE + 'Creating ' + f"{index +1}_{fileName}")
    print(Fore.WHITE)
    clip.write_videofile(f"./out/{index +1}_{fileName}", fps=30)
    print(Fore.GREEN + fileName + 'created successfully')
