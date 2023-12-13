#5.BINARY IMAGE CONVERSION(HIGH CONTRAST IMAGE)

import cv2
img = cv2.imread('abc.jpg',0) #gray scale image
cv2.imshow('GRAY SCALE IMAGE',img)#displaying the grayscale image
cv2.waitKey(2000)

#============cv2.threshold(src,thresh,max value,conversion type)
ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#converts image from grayscale to binary
#ret and binary are 2 varibales to be taken .So here ret is a dummy variable

cv2.imshow('BINARY IMAGE',binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
