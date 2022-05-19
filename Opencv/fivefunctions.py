import cv2
import numpy as np
kernel= np.ones((5,5),np.uint8)
framewidth = 230
frameheight = 100
path = "resource/hen.jpg"
img = cv2.imread(path)
#imgrs = cv2.resize(img,(framewidth,frameheight))
imgrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgrey,(5,5),0)
imgcanny = cv2.Canny(imgblur,100,100)
imgdilation = cv2.dilate(imgcanny,kernel,iterations=1)
imgerosion = cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("henn",img)
cv2.imshow("henngray",imgrey)
cv2.imshow("imgblurs",imgblur)
cv2.imshow("imgcannyy",imgcanny)
cv2.imshow("dilated",imgdilation)
cv2.imshow("erodeed",imgerosion)
cv2.waitKey(0)



