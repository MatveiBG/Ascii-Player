import PIL
import cv2
import numpy as np
import os
from divImgs import imgFrm
from imgAscii import imgToAscii
import pygame
from playsound import playsound
import time


APP_FOLDER = "D:/Documents/!_Utile_!/badApple/data"


totalFiles = 0
totalDir = 0

for base, dirs, files in os.walk(APP_FOLDER):
    print('Searching in : ',base)
    for directories in dirs:
        totalDir += 1
    for Files in files:
        totalFiles += 1


print('Total number of files',totalFiles)
print('Total Number of directories',totalDir)
print('Total:',(totalDir + totalFiles))

# mixer.init()
# mixer.music.load("blackdance.mp4")
# mixer.music.play()


pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load("badApple.mp3")
pygame.mixer.music.play()

for i in range(totalFiles):
    imgToAscii("frame" + str(i) + ".jpg")
    time.sleep(0.03)