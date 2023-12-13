#16.FACE DETECTION IN AN IMAGE
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#importing haarcascade mode
img = cv2.imread('abc.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,9)
#1.1 - ScalerFactor,9 is minNeighbors  -- Tuning Parameters


for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        #cv2.rectangle(src,start pt,end pt,color,thickness)


cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
