import cv2

framewidth = 200
frameheight = 100


cap = cv2.VideoCapture(0)
#cap.set(1000,framewidth)
#cap.set(1000,frameheight)
while True:
    success,img = cap.read()
    img = cv2.resize(img,(framewidth,frameheight))
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
