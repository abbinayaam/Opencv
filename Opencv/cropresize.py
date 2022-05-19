import cv2
import numpy as np

img = cv2.imread("resource/hen.jpg")
print(img.shape)
width , height = 1000 , 1000
imgresize = cv2.resize(img,(width,height))
print(imgresize.shape)
imgcropped = img[100:500, 90:450]
imgcropresize = cv2.resize(imgcropped,(img.shape[1],img.shape[0]))

cv2.imshow("henn",img)
cv2.imshow("resized",imgresize)
cv2.imshow("cropimage",imgcropped)
cv2.imshow("cropresize",imgcropresize)
cv2.waitKey(0)