#9.RESIZING/SCALING the IMAGE

import cv2
import numpy as np

img = cv2.imread('abc.jpg')#reading the image
cv2.imshow('ORIGINAL IMAGE',img)
cv2.waitKey(500)



#1.Let us scale down the image to 75%
img1 = cv2.resize(img,None,fx = 0.75,fy = 0.75)
cv2.imshow('SCALED DOWN IMAGE',img1)

#2.Let us scale up the image to 150%
img2 = cv2.resize(img,None,fx = 1.5,fy = 1.5)
cv2.imshow('SCALED UP IMAGE',img2)

#3.Scaling using custom dimensions
img3 = cv2.resize(img,(1000,400))
cv2.imshow('CUSTOM DIMENSIONS',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
