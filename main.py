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
  resizedVideo = baseVideo.resize((1080, 608))
  clipsData = getClipsData()
  clipsInfo = createClips(resizedVideo, clipsData)
  reelsInfo = createReels(clipsInfo, endVideo)
  saveClips(reelsInfo)

main()



# colorClip = ColorClip(size =(1080, 1920), color =[30, 30, 30], duration=10)

# footerText = addWordSpacing('Experiences 404', 6)
# textClip = TextClip(footerText, font ="./resources/BebasNeue-Regular.ttf", fontsize = 47.5, color ="#fbbc09")
# textClip = textClip.set_position(("center","bottom")).set_duration(10)

# # Top Text
# topText = TextClip(
#   'Aprende a diferenciar los recursos que consumes',
#   font ="./resources/OpenSans-ExtraBold.ttf",
#   fontsize = 53.8, color ="#ffffff",
#   method='caption',
#   align='West',
#   size=(600,200),
#   interline=1.4
# )
# topText = topText.set_position((0.1,0.1), relative=True).set_duration(10)

# # Bottom Text
# bottomText = TextClip(
#   'según tu nivel de conocimiento o experiencia',
#   font ="./resources/OpenSans-ExtraBold.ttf",
#   fontsize = 53.8, color ="#ffffff",
#   method='caption',
#   align='East',
#   size=(600,200),
#   interline=1.4
# )
# bottomText = bottomText.set_position((0.3,0.7), relative=True).set_duration(10)

# mockClip = ColorClip(size =(1080, 608), color =[255,255,255], duration=10)

# reel = CompositeVideoClip([
#   colorClip.set_start(0),
#   mockClip.set_position(("center","center")).set_start(0),
#   textClip.set_start(0),
#   topText.set_start(0),
#   bottomText.set_start(0),
# ])
# reel.write_videofile('out.mp4', fps=30)

# Next step: https://dev.to/ethand91/download-youtube-videos-with-python-4kp4
