import cv2
import numpy as np

circles = np.zeros((4,2),np.int32)
counter=0
def mousebutton(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter]=x,y
        counter = counter+1
        print(circles)

#img = cv2.imread("resource/cards.jpg")
img = cv2.imread("resource/book.png")
while True:

    if counter == 4:
        width,height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        result = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("outputing",result)

    for x in range(0,4):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),5,(0,255,0),cv2.FILLED)
        cv2.imshow("books",img)
        #cv2.imshow("cards",img)
        cv2.setMouseCallback("books",mousebutton)
        cv2.waitKey(1)
