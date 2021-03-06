import cv2
import numpy as np
import os

def imgFrm(videoPath):
    # Playing video from file:
    cap = cv2.VideoCapture(videoPath)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')

    currentFrame = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#imgFrm("badApple/badApple.mp4")
#imgFrm("rickRoll/rickRoll.mp4")
#imgFrm("superIdol/superIdol.mp4")