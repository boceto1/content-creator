from moviepy.editor import *

def createClips(baseVideo, clipTimes):
    clips = map(lambda clipTime: baseVideo.subclip(clipTime[0], clipTime[1]), clipTimes)
    return clips

def saveClips(clips):
  for index, clip in enumerate(clips):
    clip.write_videofile(f"test-clip{index}.mp4")

def main():
   baseVideo = VideoFileClip("test-video.mp4")
   clips = createClips(baseVideo, [[831, 950]])
   saveClips(clips)

main()




