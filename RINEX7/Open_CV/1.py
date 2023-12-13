#1.READ an IMAGE

import cv2 #importing the opencv/computer vision lib
img = cv2.imread('abc.jpg') #We are reading the image
cv2.imshow('OUTPUT2',img) #We are displaying the image

cv2.waitKey(0)#3000 is 3000 milliseconds,0 will make sure , the image stays forever
cv2.destroyAllWindows()
                                                                                               
