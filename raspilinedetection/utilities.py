import cv2
import numpy as np

def thresholding(image):
    """
    This function is used to threshold the image to get the binary image.
    """
    imageHSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_black=np.array([0,0,0])
    upper_black=np.array([180,255,46])
    maskBlack=cv2.inRange(imageHSV,lower_black,upper_black)
    return maskBlack

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresh

def warpImage(img,points,widht,height):
    """
    This function is used to warp the image to get the lane line.
    """
    src = np.float32(points)
    dst = np.float32([(0, height), (0, 0), (widht, 0), (widht, height)])