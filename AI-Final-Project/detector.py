import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner\\trainner_data.xml')
cascadePath = "C:\\Users\\Shuvo Khan\\Anaconda3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)
while True:
    ret, im =cam.read()
    im=cv2.resize(im,(800,600)) #resizing
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(conf)
        if(conf<47):
            if(Id==101):
                Id="SHUVO"
                print(Id)
            elif(Id==102):
                 Id="RASHED"
                 print(Id)
            elif(Id==103):
                print(Id)
                Id="BAYAZID"
                
                    
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font, 1,fontcolor)
    cv2.imshow('im',im) 
    if cv2.waitKey(10) & 0xFF==ord('q'):
                         break
cam.release()
cv2.destroyAllWindows()