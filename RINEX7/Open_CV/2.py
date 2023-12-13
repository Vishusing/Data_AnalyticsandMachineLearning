#2.Creating a Duplicate Image using Python

import cv2
img = cv2.imread('abc.jpg')#reading the image
cv2.imshow('OUTPUT 1',img)#displaying the image

cv2.imwrite('ameen.png',img)#CReates a new image

cv2.waitKey(0)
cv2.destroyAllWindows()
