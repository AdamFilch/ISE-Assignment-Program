import cv2
import numpy as np

#original image
a = cv2.imread("card.jpg")
cv2.imshow("Object - original",a)

#recolour image
b = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("Object - Recoloured",b)

#sharpened image
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=a, ddepth=-1, kernel=kernel)
cv2.imshow('Object - Sharpened', image_sharp)

#smoothed image
blur = cv2.GaussianBlur(a,(19,19),cv2.BORDER_DEFAULT)
cv2.imshow("Object - Smoothed", blur)

#edge detection
img_blur = cv2.GaussianBlur(b, (3,3), 0) ## Blur the image for better edge detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
cv2.imshow("Object - Edge Detection",edges)

#wait keydgd
cv2.waitKey(0)