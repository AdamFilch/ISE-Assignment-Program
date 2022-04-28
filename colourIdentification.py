import cv2
import numpy as np
from skimage.filters import threshold_otsu


# Resource: https://www.geeksforgeeks.org/color-identification-in-images-using-python-opencv/

img = cv2.imread("block.jpg")
image = cv2.resize(img, (700, 600))
orig = image

def kMean():

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


# Source : https://machinelearningknowledge.ai/image-segmentation-in-python-opencv/ 

def colourMask():


    rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)

    light_blue = (90, 70, 50)
    dark_blue = (128, 255, 255)

    mask = cv2.inRange(hsv_img, light_blue, dark_blue)

    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("result", result)
    cv2.waitKey(0)


    return

colourMask()