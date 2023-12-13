#8.CHECKER BOARD

import cv2
import numpy as np

img = np.zeros((200,200,3)) # BLACK BACKGROUND

img[0:100,0:100]= 255,255,255
img[100:200,100:200] = 255,255,255

cv2.imshow('CHECKER BOARD',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
