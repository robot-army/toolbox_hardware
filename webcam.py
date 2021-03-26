import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(3)
    cam1 = cv2.VideoCapture(1)
    cam2 = cv2.VideoCapture(0)

    cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    while True:
        ret_val, img = cam.read()
        ret_val1, img1 = cam1.read()
        ret_val2, img2 = cam2.read()
        img_pre = cv2.resize(img,(640,480))
        img_pre1 = cv2.resize(img1,(640,480))
        img_pre2 = cv2.resize(img2,(640,480))

        cv2.imshow('my webcam', img_pre)
        cv2.imshow('my webcam1', img_pre1)
        cv2.imshow('my webcam2', img_pre2)

        key = cv2.waitKey(1)
        if key != -1 :
            print(key)
        if key == 27: 
            cv2.imwrite('test.jpg', img)
            cv2.imwrite('test1.jpg', img1)
            cv2.imwrite('test2.jpg', img2)
 
        if key == 113:
            break

    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
