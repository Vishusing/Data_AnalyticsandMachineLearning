#11.LIVE VIDEO from the WEBCAM

import cv2

cap = cv2.VideoCapture(0) #0 here considers the default webcam port

while True:
    ret,frame = cap.read()#from the cap variable , we read the video
    #ret and frame are 2 variables to be considered
    #We only use frame variable , ret is dummy

    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1) == 13:
        break

cap.release() #It release the default webcam port 
cv2.destroyAllWindows()
