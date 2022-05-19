import cv2
import numpy as np

img = cv2.imread("resource/cards.jpg")

width,height = 250,350
pts1 = np.float32([[492,586],[686,604],[468,868],[662,885]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
result = cv2.warpPerspective(img,matrix,(width,height))


for x in range(0,4):

    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),5,(0,255,0),cv2.FILLED)





cv2.imshow("cards",img)
cv2.imshow("outputimg",result)
cv2.waitKey(0)
cv2.destroyAllWindows()