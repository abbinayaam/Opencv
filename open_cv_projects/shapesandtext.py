import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)

#img[:]= 0,0,255
imgline = cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),5)
imgcircle = cv2.circle(img,(180,180),60,(0,255,0),cv2.FILLED)
imgrect = cv2.rectangle(img,(200,300),(300,200),(0,255,0),cv2.FILLED)
imgtext = cv2.putText(img,"i love Adhiyann",(70,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),5)
#cv2.imshow("color",img)
cv2.imshow("image",img)

cv2.waitKey(0)