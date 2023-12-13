#13.RECTANGLE/SQUARE

import cv2
import numpy as np

img = np.zeros((850,850,3))

#src,starting point,end point,color,thickness
cv2.rectangle(img,(200,200),(450,450),(0,255,0),5)


cv2.imshow('Rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
