from utils import loadJsonFile;

BACKGROUND_COLOR = '#1e1e1e'

BEBAS_NEUE_FONT = './resources/BebasNeue-Regular.ttf'
FOOTER_TEXT_COLOR = "#fbbc09"

OPEN_SANS_EXTRA_BOLD_FONT = './resources/OpenSans-ExtraBold.ttf'
GENERAL_TEXT_COLOR = "#ffffff"

class GlobalStyles:
    _instance = None
    def __init__(self, styles):
        if GlobalStyles._instance is not None:
            raise Exception("Singleton class should not be instantiated more than once.")
        self.styles = self._configureStyles(styles)

    def _configureStyles (self, styles):
      globalStyles = {}
      # Add Background Color
      globalStyles['backgroundColor'] = styles['backgroundColor'] if 'backgroundColor' in styles else BACKGROUND_COLOR

       # Add General Text
      if 'generalText' in styles:
        globalStyles['generalText'] = {
          "font": styles['generalText']['font'],
          "color": styles['generalText']['color']
        }
      else:
        globalStyles['generalText'] = {
          "font": OPEN_SANS_EXTRA_BOLD_FONT,
          "color": GENERAL_TEXT_COLOR
        }

      if 'footerText' in styles:
        globalStyles['footerText'] = {
          "font": styles['footerText']['font'],
          "color": styles['footerText']['color']
        }
      else:
        globalStyles['footerText'] = {
          "font": BEBAS_NEUE_FONT,
          "color": FOOTER_TEXT_COLOR
        }

      return globalStyles

    @classmethod
    def get_instance(cls, styles={}):
        if cls._instance is None:
            cls._instance = GlobalStyles(styles)
        return cls._instance
    
    @property
    def backgroundColor (self):
        return self.styles['backgroundColor']

    @property
    def generalText (self):
        return self.styles['generalText']
    
    @property
    def footerText (self):
        return self.styles['footerText']  
    
