#22 CANNY VIDEO 
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()  #cap is frames(variable)
    canny = cv2.Canny(frame,20,150)  #100,150 are threshold values for best video# less noise   (any value b/w 0 to 255)
    cv2.imshow('My Live Sketch',canny)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()