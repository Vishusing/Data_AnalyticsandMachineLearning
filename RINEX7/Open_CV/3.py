#3.Read the INFORMATION about the image

import cv2
img = cv2.imread('abc.jpg')
print(img.shape)


#OUTPUT: (344, 612, 3)
#344 is the Height of the Image in Pixels
#612 is the Width od the Image in Pixels
#3 is the depth/channel value - 3 by default(3 primary colors)
