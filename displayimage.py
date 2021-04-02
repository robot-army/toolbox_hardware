import cv2

img =  cv2.imread('test.jpg')

while True:
    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("test",img)
    key=cv2.waitKey(0)
    if key==27:
        break
