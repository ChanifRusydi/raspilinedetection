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
cv2.createTrackbar("Hue Max", window_name, 0,179., empty)
cv2.createTrackbar("Sat Min", window_name, 0,255., empty)
cv2.createTrackbar("Sat Max", window_name, 0,255., empty)
cv2.createTrackbar("Val Min", window_name, 0,255., empty)
cv2.createTrackbar("Val Max", window_name, 0,255., empty)

cap=cv2.VideoCapture()
fpscounter=0

while True:
    fpscounter+=1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT)==fpscounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES,)
        fpscounter=0
    _, img=cap.read()
    imgSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("Hue Min", window_name)
    h_max=cv2.getTrackbarPos("Hue Max", window_name)
    s_min=cv2.getTrackbarPos("Sat Min", window_name)
    s_max=cv2.getTrackbarPos("Sat Max", window_name)
    v_min=cv2.getTrackbarPos("Val Min", window_name)
    v_max=cv2.getTrackbarPos("Val Max", window_name)
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgSV,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)

    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,result])
    cv2.imshow(window_name,hstack)
    if cv2.waitKey(1)==27:
        break

cap.release()
cap.destroyAllWindows()