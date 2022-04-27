import cv2
import numpy as np


# Resource: https://www.geeksforgeeks.org/color-identification-in-images-using-python-opencv/

def kMean():

    img = cv2.imread("waterbottle.jpg")
    image = cv2.resize(img, (700, 600))
    orig = image

    image = np.float32(image)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 60
    attempts=10

    ret,label,center=cv2.kmeans(image,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape((image.shape))


    cv2.imshow("result", result_image)

    cv2.waitKey(0)

    return

def 

kMean()