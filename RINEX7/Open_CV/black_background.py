#BLACK
# create white background using open cv and numpy
import numpy as np
import cv2

img =np.zeros((500,450,3))#250 is length,250 is breadth,3 is channel related to RGB
#change 250,250,3 to 200,200,3 and check
cv2.imshow("BLACK Background",img)
cv2.waitkey(0)
cv2.destroyAllWindows()