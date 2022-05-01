import cv2
import numpy as np

#original image
a = cv2.imread("card.jpg")


def menu():
    print("Choose your image enhancement: ")
    print("1. Recolour Image")
    print("2. Sharpened Image")
    print("3. Smoothed Image")
    print("4. Edge Detection")
    print("5. Noise Reduction")
    print("6. Exit")
    print(": ")

menu()
choice = int(input())

if(choice == 1):
    b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Objcet - Original",a)
    cv2.imshow("Object - Recoloured", b)

elif(choice == 2):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=a, ddepth=-1, kernel=kernel)
    cv2.imshow("Objcet - Original", a)
    cv2.imshow('Object - Sharpened', image_sharp)

elif(choice == 3):
    blur = cv2.GaussianBlur(a,(19,19),cv2.BORDER_DEFAULT)
    cv2.imshow("Objcet - Original", a)
    cv2.imshow("Object - Smoothed", blur)

elif(choice == 4):
    b = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(b, (3,3), 0) ## Blur the image for better edge detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    cv2.imshow("Object - Original", a)
    cv2.imshow("Object - Edge Detection",edges)

elif(choice == 5):
    lol = cv2.imread("noiseCard.png")
    noised = cv2.fastNlMeansDenoisingColored(lol,None,30,20,5,10)
    cv2.imshow("Object - Noise", lol)
    cv2.imshow("Object - Noise Reduced", noised)

elif(choice == 6):
    print("waiting for adam for exit file.")

else:
    print("Wrong input number! Try Again!")
    menu()


#wait keydgd
cv2.waitKey(0)
menu()