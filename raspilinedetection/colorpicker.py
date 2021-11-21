import numpy as np
import cv2

frameWidth=640
frameHeight=480
capture=cv2.VideoCapture(1)
capture.set(3, frameWidth)
capture.set(4, frameHeight)

window_name="Color Picker"
cv2.namedWindow(window_name)
cv2.resizeWindow(window_name,640,480)
cv2.createTrackbar("Hue Min", window_name, 0,179., empty)




cap=cv2.VideoCapture()
fpscounter=0
while True:
    fpscounter+=1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT)==fpscounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES,)
        fpscounter=0
    _, img=cap.read()
    imgSV=cv2.cvtColor(img,cv2.COLOR_BGR2HS0)