#24 FACE AND EYE DETECTION 

#face recognition eye and face
import cv2
a = cv2.imread("abc.jpg")

model_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

demo_face = model_face.detectMultiScale(a,1.1,9)
demo_eye = model_eye.detectMultiScale(a,1.1,18)

for (x,y,w,h) in demo_face:#15 times looping
	cv2.rectangle(a, (x, y), (x + h, y + w), (255, 100, 0), 5)
	cv2.imshow('Output', a)
	
for (x,y,w,h) in demo_eye:  #30 times looping
        cv2.rectangle(a, (x, y), (x + h, y + w), (0, 255, 255), 5)
        cv2.imshow('Output', a)
    
cv2.waitKey(0)
cv2.destroyAllWindows()
