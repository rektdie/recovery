import os
import shutil

path = "F:/Munka/14i/A_cs/Kasa Mark/PowerPoint/Geoguessr.pptx"
destination = "D:/Geoguessr.pptx"

def MoveFiles():
    shutil.copyfile(path, destination)

while True:
    if os.path.exists(path):
        MoveFiles()
        break