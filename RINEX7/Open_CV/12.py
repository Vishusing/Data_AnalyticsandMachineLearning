#12.MY CANNY(EDGE DETECTION TECHNIQUE) SKETCH

import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    canny = cv2.Canny(frame,20,150)#20,150 are the threshold values for best edge detection
    cv2.imshow('MY CANNY SKETCH',canny)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
