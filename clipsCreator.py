from utils import toCamelCase, createOutDir
from colorama import Fore
from moviepy.editor import *
from constants import getFooterText, REELS_DIMENSION, VIDEO_DIMENSION, getTopTextClip, getBottomTextClip, MOCK_CLIP, MOCK_DEFAULT_DURATION

def createClip(baseVideo, clipData):
  startTime, endTime = clipData['time']
  clip = baseVideo.subclip(startTime, endTime)
  return clip

def createClips(baseVideo, clipsData):
    clips = map(lambda clipData: createClip(baseVideo, clipData), clipsData)
    return clips

def createReel(clipWithInfo, endVideo, footerText, isPreview):
  clip, clipInfo = clipWithInfo
  topText, bottomText = clipInfo['text']
  clipDuration = MOCK_DEFAULT_DURATION if isPreview else clip.duration

  baseVideoShape = ColorClip(size =(REELS_DIMENSION[0], REELS_DIMENSION[1]), color =[30, 30, 30], duration=clipDuration)

  styeledFooterText = getFooterText(footerText).set_duration(clipDuration)
  topTextClip = getTopTextClip(topText).set_duration(clipDuration)
  bottomTextClip = getBottomTextClip(bottomText).set_duration(clipDuration)

  clips = [
    baseVideoShape.set_start(0),
    styeledFooterText.set_start(0),
    topTextClip.set_start(0),
    bottomTextClip.set_start(0),
  ]

  if isPreview:
    clips.extend([
      MOCK_CLIP.set_duration(clipDuration).set_position(("center","center")).set_start(0),
    ])
  else:
    clips.extend([
      clip.set_position(("center","center")).set_start(0),
      endVideo.set_start(clipDuration).crossfadein(1.5),
    ])

  reel = CompositeVideoClip(clips)
  
  return reel

# reelsInfo: { baseVideo, clipsInfo, endClip, footerText }
def createReels(reelsInfo, isPreview):
  baseVideo,clipsInfo, endClip, footerText = reelsInfo['baseVideo'], reelsInfo['clipsInfo'], reelsInfo['endClip'], reelsInfo['footerText']
  clips = createClips(baseVideo, clipsInfo)
  clipsWithInfo = zip(clips, clipsInfo)
  reels = map(lambda clipWithInfo: createReel(clipWithInfo, endClip, footerText, isPreview), clipsWithInfo)
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

def generateReels(projectData, isPreview):
  baseVideo = VideoFileClip(projectData['baseVideo'])
  endClip = VideoFileClip(projectData['endClip'])
  resizedVideo = baseVideo.resize((VIDEO_DIMENSION[0], VIDEO_DIMENSION[1]))

  reelsInfo = {
    'baseVideo': resizedVideo,
    'clipsInfo': projectData['clips'],
    'endClip': endClip,
    'footerText': projectData['footerText'],
  }
  reels = createReels(reelsInfo, isPreview)
  saveClips(projectData['projectName'], projectData['clips'], reels)
