# If you are using pycharm go to settings -> project xyx->python interpr ADD opencv-python and mediapipe


import cv2 as cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands() #to check param ctrl +click
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks) to check if its detecting hands
    #print(img)
    #To extract hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for  id,lm in enumerate(handLms.landmark): #to extract cordinates
                #print(id,lm)
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
                if id==0: # ID 0 IS WRIST
                    cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)#This is a single hand
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
