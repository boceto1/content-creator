from re import sub
from moviepy.editor import ColorClip

def toCamelCase(string):  
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")  
    return string[0].lower() + string[1:]  

def addWordSpacing(string, spacing=1):
    return (" "*spacing).join(list(string))


mockClip = ColorClip(size =(1080, 608), color =[255,255,255])
