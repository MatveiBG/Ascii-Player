import PIL
import cv2
import numpy as np
import os
from divImgs import imgFrm
from imgAscii import imgToAscii
import pygame
from playsound import playsound
import time


appleData = "dataApple"
rickRollData = "dataRickRoll"
superIdolData = "dataSuperIdol"




def fileCount(direc):
    totalFiles = 0
    totalDir = 0
    for base, dirs, files in os.walk(direc):
        print('Searching in : ',base)
        for directories in dirs:
            totalDir += 1
        for Files in files:
            totalFiles += 1
    return totalFiles

applefiles =  fileCount(appleData)
rickRollfiles =  fileCount(rickRollData)
superIdolfiles =  fileCount(superIdolData)


quest = 0
while quest!="1" and quest!="2" and quest!="3":
    quest = input("Bad Apple (1) or Never gonna give you up (2) or Super Idol (3): ")

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

if quest == "1":
    pygame.mixer.music.load("badApple/badApple.mp3")
    pygame.mixer.music.play()
    for i in range(applefiles):
        imgToAscii("dataApple/frame" + str(i) + ".jpg")
        time.sleep(0.03)

elif quest == "2":
    pygame.mixer.music.load("rickRoll/rickRoll.mp3")
    pygame.mixer.music.play()
    for i in range(rickRollfiles):
        imgToAscii("dataRickRoll/frame" + str(i) + ".jpg")
        time.sleep(0.022)

elif quest == "3":
    pygame.mixer.music.load("superIdol/superIdol.mp3")
    pygame.mixer.music.play()
    for i in range(rickRollfiles):
        imgToAscii("datasuperIdol/frame" + str(i) + ".jpg")
        time.sleep(0.015)




