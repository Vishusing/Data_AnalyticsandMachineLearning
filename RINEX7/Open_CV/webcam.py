#21 SHOWING LIVE VIDEO FROM WEBCAM
import cv2

cap = cv2.VideoCapture(0)    #0 takes default camera of laptop

while True:   #takes lot of frames continuously and displays 
    ret,frame = cap.read()    #read the port #tuple returned 
    #ret and frame are the 2 variables to be taken ,but only frame will be used ,and ret is not used,but ret should be ther
    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1) == 13:   #to quit press enter ASCII value of enter is 13
        break
 
cap.release()    #release the port  else port of webcam can get damaged
cv2.destroyAllWindows()

