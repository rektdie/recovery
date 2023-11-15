import os
import shutil
import time

path = "M:/Munka/14i/A_cs/Kasa Mark/PowerPoint/Geoguessr.pptx"
destination = "D:/Geoguessr.pptx"

def MoveFiles():
    start = time.perf_counter()
    shutil.copyfile(path, destination)
    end = time.perf_counter()
    print(f"Moved in {end-start}")

def Main():
    print("Waiting")
    while True:
        if os.path.exists(path):
            MoveFiles()
            break

if __name__ == "__main__":
    Main()