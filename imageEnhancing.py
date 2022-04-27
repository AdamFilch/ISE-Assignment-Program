import cv2
import numpy as np

a = cv2.imread("card.jpg")
cv2.imshow("Object - original",a)

b = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("Object - Recoloured",b)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=a, ddepth=-1, kernel=kernel)
cv2.imshow('Object - Sharpened', image_sharp)

blur = cv2.GaussianBlur(a,(19,19),cv2.BORDER_DEFAULT)
cv2.imshow("Object - Smoothed", blur)

cv2.waitKey(0)