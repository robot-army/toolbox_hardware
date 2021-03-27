import cv2
import os
import datetime


def show_webcam(mirror=False):

    mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(mydir)

    cam = cv2.VideoCapture(4) # picam, max res 2592 1944
    cam1 = cv2.VideoCapture(2) # webcam 1, max res 1920 1080
    cam2 = cv2.VideoCapture(0) # webcam 0, max res 1920 1080


    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)
    cam1.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cam2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

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
            i = 0
            while os.path.exists(mydir+"/camera1_%s.jpg" % i):
                i += 1

            cv2.imwrite(mydir+'/camera1_'+str(i)+'.jpg', img)
            cv2.imwrite(mydir+'/camera2_'+str(i)+'.jpg', img1)
            cv2.imwrite(mydir+'/camera3_'+str(i)+'.jpg', img2)
            print("Saved images")

 
        if key == 113:
            break

    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
