#7.SOLID COLORS (RED,GREEN and BLUE)

#RED
import cv2
import numpy as np
img = np.zeros((250,250,3)) #creates a black image

img[:] = 0,0,255 #Assigning the color(B,G,R)

cv2.imshow('RED',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


img = np.zeros((250,250,3)) #creates a black image

img[:] = 0,255,0 #Assigning the color(B,G,R)

cv2.imshow('GREEN',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


img = np.zeros((250,250,3)) #creates a black image

img[:] = 255,0,0 #Assigning the color(B,G,R)

cv2.imshow('BLUE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


