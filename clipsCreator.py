from utils import toCamelCase
from os import mkdir, path, rmdir
from colorama import Fore
from moviepy.editor import *
from utils import addWordSpacing, mockClip
import shutil

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

def createReel(clipInfo, endVideo):
  fileName, clip = clipInfo
  # clipDuration = clip.duration
  clipDuration = 2

  colorClip = ColorClip(size =(1080, 1920), color =[30, 30, 30], duration=clipDuration)

  footerText = getFooterText().set_duration(clipDuration)

  # Top Text
  topText = TextClip(
    'Aprende a diferenciar los recursos que consumes',
    font ="./resources/OpenSans-ExtraBold.ttf",
    fontsize = 60, color ="#ffffff",
    method='caption',
    align='West',
    size=(756,300),
    interline=1.4
  )
  topText = topText.set_position((0.1,0.1), relative=True).set_duration(10)

  topText.text = 'lalalalal'

  # Bottom Text
  bottomText = TextClip(
    'según tu nivel de conocimiento o experiencia',
    font ="./resources/OpenSans-ExtraBold.ttf",
    fontsize = 60, color ="#ffffff",
    method='caption',
    align='East',
    size=(756,300),
    interline=1.4
  )


  bottomText = bottomText.set_position((0.2,0.75), relative=True).set_duration(10)

  endVideo = VideoFileClip('./templates/endVideo.mp4')

  reel = CompositeVideoClip([
    colorClip.set_start(0),
    mockClip.set_duration(clipDuration).set_position(("center","center")).set_start(0),
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
  if path.exists('./out'):
    shutil.rmtree('./out')
  mkdir('./out')
  for index, clipInfo in enumerate(clipsInfo):
    fileName, clip = clipInfo
    print(Fore.BLUE + 'Creating ' + f"{index +1}_{fileName}")
    print(Fore.WHITE)
    clip.write_videofile(f"./out/{index +1}_{fileName}", fps=30)
    print(Fore.GREEN + fileName + 'created successfully')
