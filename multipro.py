
import time
import numpy as np
import cv2 as cv
import glob
from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count


width = 9
height = 10
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((height*width,3), np.float32)
objp[:,:2] = np.mgrid[0:width,0:height].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

def corners(fname):

    img = cv.imread(fname)
    print("Loading "+fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, (width,height),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (width,height), corners2, ret)
        print("Found corners in "+fname)
        return objp, corners

def main():

    start = timer()

    print(f'starting computations on {cpu_count()} cores')

    values = glob.glob('2021-04-01_21-27-40/camera1*.jpg')

    img_sizer = cv.imread(values[1])
    gray_sizer = cv.cvtColor(img_sizer, cv.COLOR_BGR2GRAY)

    with Pool() as pool:
        returned = pool.map(corners, values)
        for i in returned:
            if i != None:
                objpoints.append(i[0])
                imgpoints.append(i[1])

    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray_sizer.shape[::-1], None, None)
    print(ret,mtx,dist,rvecs,tvecs)

    end = timer()

    print(f'elapsed time: {end - start}')

if __name__ == '__main__':
    main()

