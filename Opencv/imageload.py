import cv2


def imageloadfn():
    img=cv2.imread("resource/hen.jpg",-1)
    cv2.imshow("henpic",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

