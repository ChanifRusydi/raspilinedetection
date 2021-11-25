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

def warpImage(img,points,width,height,inv=False):
    """
    This function is used to warp the image to get the lane line.
    """
    src = np.float32(points)
    dst = np.float32([(0, height), (0, 0), (width, 0), (width, height)])
    if inv:
        M = cv2.getPerspectiveTransform(dst, src)
    else:
        M=cv2.getPerspectiveTransform(src,dst)

    warped = cv2.warpPerspective(img, M, (width, height))
    return warped
    # M = cv2.getPerspectiveTransform(src, dst)
    # Minv = cv2.getPerspectiveTransform(dst, src)
def initializeTrackbars(intialTracbarVals,widthTrackbar=500,heightTrackbar=500): 
    """
    This function is used to initialize the trackbars.
    """
    cv2.namedWindow("Trackbars", 0)
    for i in range(len(intialTracbarVals)):
        cv2.createTrackbar(str(trackbarName[i]), "Trackbars", intialTracbarVals[i], maxIntensity[i], nothing)

def drawPoints(image,points):
    """
    This function is used to draw the points on the image.
    """
    for i in range(len(points)):
        cv2.circle(image, points[i], 10, (0,0,255), -1)
    return image

def getHistogram(image):
    """
    This function is used to get the histogram of the image.
    """
    histogram=np.sum(image[image.shape[0]//2:,:],axis=0)
    return histogram

def stackImages(scale,imgArray):
    """
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(
        hor = np.hstack(imgArray)
        ver = np.vstack(hor)
    return ver



