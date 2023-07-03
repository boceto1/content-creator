from utils import toCamelCase, createOutDir
from colorama import Fore
from moviepy.editor import *
from constants import FOOTER_TEXT, REELS_DIMENSION, MOCK_CLIP, getTopTextClip, getBottomTextClip

def createClip(baseVideo, clipData):
  name,startTime,endTime, topText, bottomText = clipData
  clip = baseVideo.subclip(startTime, endTime)
  fileName = toCamelCase(name) + '.mp4'
  text = [topText, bottomText]
  return [fileName, clip, text]

def createClips(baseVideo, clipsData):
    clips = map(lambda clipData: createClip(baseVideo, clipData), clipsData)
    return clips

def createReel(clipInfo, endVideo):
  fileName, clip, text = clipInfo
  topText, bottomText = text
  clipDuration = clip.duration

  baseVideoShape = ColorClip(size =(REELS_DIMENSION[0], REELS_DIMENSION[1]), color =[30, 30, 30], duration=clipDuration)

  footerText = FOOTER_TEXT.set_duration(clipDuration)
  topTextClip = getTopTextClip(topText).set_duration(clipDuration)
  bottomTextClip = getBottomTextClip(bottomText).set_duration(clipDuration)

  endVideo = VideoFileClip('./templates/endVideo.mp4')

  reel = CompositeVideoClip([
    baseVideoShape.set_start(0),
    clip.set_position(("center","center")).set_start(0),
    footerText.set_start(0),
    topTextClip.set_start(0),
    bottomTextClip.set_start(0),
    endVideo.set_start(clipDuration).crossfadein(1.5)
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
