from moviepy.editor import TextClip, ColorClip
from utils import addWordSpacing

BEBAS_NEUE_FONT = './resources/BebasNeue-Regular.ttf'
OPEN_SANS_EXTRA_BOLD_FONT = './resources/OpenSans-ExtraBold.ttf'

FOOTER_TEXT_COLOR = "#fbbc09"
INFORMATION_TEXT_COLOR = "#ffffff"

def _getFooterText():
  footerText = addWordSpacing('Experiences 404', 6)
  textClip = TextClip(footerText, font = BEBAS_NEUE_FONT, fontsize = 47.5, color = FOOTER_TEXT_COLOR)
  textClip = textClip.set_position(("center","bottom"))
  return textClip

FOOTER_TEXT = _getFooterText()

REELS_DIMENSION = [1080, 1920]

VIDEO_DIMENSION = [1080, 608]

def getTopTextClip(text): 
  return TextClip(
    text,
    font = OPEN_SANS_EXTRA_BOLD_FONT,
    fontsize = 60, color = INFORMATION_TEXT_COLOR,
    method='caption',
    align='West',
    size=(756,300),
    interline=1.4
  ).set_position((0.1,0.1), relative=True)

def getBottomTextClip(text):
  return TextClip(
    text,
    font = OPEN_SANS_EXTRA_BOLD_FONT,
    fontsize = 60, color = INFORMATION_TEXT_COLOR,
    method='caption',
    align='East',
    size=(756,300),
    interline=1.4
  ).set_position((0.2,0.75), relative=True)

# You can use MOCK CLIP in the following way: MOCK_CLIP.set_duration(clipDuration).set_position(("center","center")).set_start(0),
MOCK_CLIP = ColorClip(size =(VIDEO_DIMENSION[0], VIDEO_DIMENSION[1]), color =[255,255,255])
