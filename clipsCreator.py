from utils import toCamelCase, createOutDir
from colorama import Fore
from moviepy.editor import *
from constants import getFooterText, REELS_DIMENSION, VIDEO_DIMENSION, getTopTextClip, getBottomTextClip

def createClip(baseVideo, clipData):
  startTime, endTime = clipData['time']
  clip = baseVideo.subclip(startTime, endTime)
  return clip

def createClips(baseVideo, clipsData):
    clips = map(lambda clipData: createClip(baseVideo, clipData), clipsData)
    return clips

def createReel(clipWithInfo, endVideo):
  clip, clipInfo = clipWithInfo
  topText, bottomText = clipInfo['text']
  clipDuration = clip.duration

  baseVideoShape = ColorClip(size =(REELS_DIMENSION[0], REELS_DIMENSION[1]), color =[30, 30, 30], duration=clipDuration)

  footerText = getFooterText().set_duration(clipDuration)
  topTextClip = getTopTextClip(topText).set_duration(clipDuration)
  bottomTextClip = getBottomTextClip(bottomText).set_duration(clipDuration)

  reel = CompositeVideoClip([
    baseVideoShape.set_start(0),
    clip.set_position(("center","center")).set_start(0),
    footerText.set_start(0),
    topTextClip.set_start(0),
    bottomTextClip.set_start(0),
    endVideo.set_start(clipDuration).crossfadein(1.5)
  ])
  
  return reel

def createReels(baseVideo, clipsInfo, endVideo):
  clips = createClips(baseVideo, clipsInfo)
  clipsWithInfo = zip(clips, clipsInfo)
  reels = map(lambda clipWithInfo: createReel(clipWithInfo, endVideo), clipsWithInfo)
  return reels

def saveClips(projectName, clipsInfo, reels):
  dirName = toCamelCase(projectName)
  createOutDir(f'./{dirName}')
  for index, reel in enumerate(reels):
    clipInfo = clipsInfo[index]
    fileName = toCamelCase(clipInfo['name'])
    print(Fore.BLUE + 'Creating ' + f"{index + 1}_{fileName}")
    print(Fore.WHITE)
    reel.write_videofile(f"./{dirName}/{index +1}_{fileName}.mp4", fps=30)
    print(Fore.GREEN + fileName + 'created successfully')

def generateReels(projectData):
  baseVideo = VideoFileClip(projectData['baseVideo'])
  endClip = VideoFileClip(projectData['endClip'])
  resizedVideo = baseVideo.resize((VIDEO_DIMENSION[0], VIDEO_DIMENSION[1]))
  reels = createReels(resizedVideo, projectData['clips'], endClip)
  saveClips(projectData['projectName'], projectData['clips'], reels)
