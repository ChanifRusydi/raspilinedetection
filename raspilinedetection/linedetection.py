import cv2
import numpy as np
import utilites as ut

curveList = []
avgvalue = 0

def getLaneCurve(img,display=2):
    imageCopy=img.copy()
    imageResul=img.copy()
    imageThres=ut.thresholding(img)

    heighThreshold,widththreshold,color=img.shape
    points=ut.val


