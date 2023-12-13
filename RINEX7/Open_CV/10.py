#10.RECTANGLE/SQUARE

import cv2
import numpy as np

img = np.zeros((500,500,3)) #black background

#cv2.rectangle(src,point1,point2,color,thickness)
cv2.rectangle(img,(200,200),(400,400),(0,255,0),5)
cv2.imshow('RECTANGLE',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
