import cv2
import numpy as np


framewidth = 650
frameheight = 450
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",450,300)
cv2.createTrackbar("Hmin","HSV",0,179,empty)
cv2.createTrackbar("Hmax","HSV",179,179,empty)
cv2.createTrackbar("Smin","HSV",0,255,empty)
cv2.createTrackbar("Smax","HSV",255,255,empty)
cv2.createTrackbar("Vmin","HSV",0,255,empty)
cv2.createTrackbar("Vmax","HSV",255,255,empty)

while True:

    success,img = cap.read()
    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hmin","HSV")
    h_max = cv2.getTrackbarPos("Hmax", "HSV")
    s_min = cv2.getTrackbarPos("Smin","HSV")
    s_max = cv2.getTrackbarPos("Smax","HSV")
    v_min = cv2.getTrackbarPos("Vmin","HSV")
    v_max = cv2.getTrackbarPos("Vmax","HSV")
    print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask = mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img,mask,result])

    #cv2.imshow("video", img)
    #cv2.imshow("HSVimg", imghsv)
    #cv2.imshow("mask",mask)
    #cv2.imshow("resultimg",result)
    cv2.imshow("stack", hstack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
cap.release()
cv2.destroyAllWindows()




























