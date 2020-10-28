import cv2
import numpy as np

    
def draw():
    face_cascade =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret,img = cap.read()
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w] ## searching for eyes only inside face region
            roi_color = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            centre_x = 0
            centre_y = 0
            for (ex,ey,ew,eh) in eyes:
                centre_x = int(((2*ex) + ew)/2)
                centre_y = int(((2*ey) + eh)/2)
                cv2.circle(roi_color,(centre_x,centre_y),10,(0,0,255),2)
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #centre_x = int(centre_x/2)
            #centre_y = int(centre_y/2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

draw()
