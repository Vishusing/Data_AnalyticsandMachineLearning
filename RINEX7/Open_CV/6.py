#6.SOLID BACKGROUND(BLACK or WHITE BACKGROUND)
#WHITE COLOR

import cv2
import numpy as np

img = np.ones((500,500,3))#500 is the length,500 is the width,3 is depth/channel value
#In the above line , we are creating a white background

cv2.imshow('WHITE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#BLACK COLOR

img = np.zeros((500,500,3))#500 is the length,500 is the width,3 is depth/channel value
#In the above line , we are creating a white background

cv2.imshow('BLACK',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
