import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
#loading haarclassifier
eye_cascade=cv2.CascadeClassifier('C:/Users/mouryasashank/data/haarcascade_lefteye_2splits.xml')
s=0
# load the saved model:
classifier = load_model('eye02.h5')

def detect_eye(img):
    eye_img=img.copy()
    #gray_img=cv2.cvtColor(eye_img,cv2.COLOR_BGR2GRAY)
    eye_rect=eye_cascade.detectMultiScale(eye_img)
    for (x,y,w,h) in eye_rect:
        cv2.rectangle(eye_img,(x,y),(x+w,y+h),(255,0,0),1)
        crop_image = frame[y:y + h, x:x + w]
        cv2.imwrite("D:/imgs/" + "eye.0" + ".jpg", crop_image)
    return eye_img
def predicts():
    a=['open','close']
    # load the images :
    img1 = image.load_img('D:/imgs/eye.0.jpg', target_size=(24,24,1))
    pre = image.img_to_array(img1)
    pred = np.expand_dims(pre, axis=0)
    pr = classifier.predict(pred)
    #print(pr)
    if pr[0][1] == 1:
       a= 'open'
    else:
        a= 'close'
    return a
cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
    ret,frame=cap.read()
    h,w=frame.shape[:2]
    frame=detect_eye(frame)
    a = predicts()
    if a=='open':
        s=0
        cv2.putText(frame, "score:" + str(s), (100, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, "Open", (10,50), font, 1, (255, 0, 0), 1, cv2.LINE_AA)
    else:
        s=s+1
        cv2.putText(frame, "score:" + str(s), (100, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, "closed", (10,50), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
        if (s>14):
            cv2.putText(frame,"WARNING:You are Sleepy",(250,50),font,1,(0,0,139),1,cv2.LINE_AA)
            #cv2.putText(frame, "score:" + str(s)+"  WARNING ", (200, 50), font, 1, (255, 255, 0), 1, cv2.LINE_AA)
    cv2.imshow('eye_detect',frame)
    k = cv2.waitKey(1)
    if k & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
