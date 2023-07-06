from moviepy.editor import TextClip, ColorClip
from utils import addWordSpacing
from GlobalStyles import GlobalStyles

def getFooterText():
  styles = GlobalStyles.get_instance()
  font, color = styles.footerText['font'], styles.footerText['color']

  footerText = addWordSpacing('Experiences 404', 6)
  textClip = TextClip(footerText, font = font, fontsize = 47.5, color = color)
  textClip = textClip.set_position(("center","bottom"))
  return textClip

REELS_DIMENSION = [1080, 1920]

VIDEO_DIMENSION = [1080, 608]

def getTopTextClip(text): 
  styles = GlobalStyles.get_instance()
  font, color = styles.generalText['font'], styles.generalText['color']
  return TextClip(
    text,
    font = font,
    fontsize = 60, color = color,
    method='caption',
    align='West',
    size=(756,300),
    interline=1.4
  ).set_position((0.1,0.1), relative=True)

def getBottomTextClip(text):
  styles = GlobalStyles.get_instance()
  font, color = styles.generalText['font'], styles.generalText['color']
  return TextClip(
    text,
    font = font,
    fontsize = 60, color = color,
    method='caption',
    align='East',
    size=(756,300),
    interline=1.4
  ).set_position((0.2,0.75), relative=True)

# You can use MOCK CLIP in the following way: MOCK_CLIP.set_duration(clipDuration).set_position(("center","center")).set_start(0),
MOCK_CLIP = ColorClip(size =(VIDEO_DIMENSION[0], VIDEO_DIMENSION[1]), color =[255,255,255])
MOCK_DEFAULT_DURATION = 2
