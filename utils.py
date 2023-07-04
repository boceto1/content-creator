from re import sub
import shutil
from os import mkdir, path
import json

def toCamelCase(string):  
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")  
    return string[0].lower() + string[1:]  

def addWordSpacing(string, spacing=1):
    return (" "*spacing).join(list(string))

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")  # Remove the '#' symbol if present
    red = int(hex_code[0:2], 16)  # Extract and convert the red component
    green = int(hex_code[2:4], 16)  # Extract and convert the green component
    blue = int(hex_code[4:6], 16)  # Extract and convert the blue component
    return (red, green, blue)  # Return the RGB values as a tuple

def createOutDir(outDirPath):
  if path.exists(outDirPath):
    shutil.rmtree(outDirPath)
  mkdir(outDirPath)

def loadJsonFile(path):
   with open(path, "r") as json_file:
    # Load the JSON data
    json_data = json.load(json_file)
    return json_data

def createJsonFile(path, jsonData):
   with open(path, "w") as json_file:
    json.dump(jsonData, json_file, indent=2)
