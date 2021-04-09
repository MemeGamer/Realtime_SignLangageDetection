import cv2
import numpy as np
import HandTrackingModule as htm
import math
from gtts import gTTS
import os
from playsound import playsound
import time

import TextToSpeech as ts

def signlanguage():
    wCam, hCam =640, 480
    cenx=320
    ceny=240
    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)
    pTime=0
    detector =htm.handDetector(detectionCon=0.7)
    Detection=""
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img=detector.findHands(img)
        lmList = detector.findPosition(img,draw=False)
        cv2.circle(img, (cenx,ceny), 5, (0, 0, 255), cv2.FILLED)
        if len(lmList)!=0:
            ts.text_to_speech("Hand")
            #print(lmList[8],lmList[5])
            x1,y1 = lmList[8][1],lmList[8][2]
            x2, y2 = lmList[5][1], lmList[5][2]

            u1, v1 = lmList[12][1], lmList[12][2]
            u2, v2 = lmList[9][1], lmList[9][2]

            w1, k1 = lmList[16][1], lmList[16][2]
            w2, k2 = lmList[13][1], lmList[13][2]

            z1, r1 = lmList[20][1], lmList[20][2]
            z2, r2 = lmList[17][1], lmList[17][2]

            m1, n1 = lmList[4][1], lmList[4][2]
            m2, n2 = lmList[9][1], lmList[9][2]


        #Center
            q2, p2 = lmList[0][1], lmList[0][2]
            cx, cy = lmList[10][1], lmList[10][2]
            #cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(img,(x1,y1),5,(255,0,255),cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (255, 0, 255), cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),2)
            cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)

            length=math.hypot(x2-x1,y2-y1)
            length1 = math.hypot(u2 - u1, v2 - v1)
            length2 = math.hypot(w2 - w1, k2 - k1)
            length3 = math.hypot(z2 - z1, r2 - r1)
            length4 = math.hypot(m2 - m1, n2 - n1)
            whatlen = math.hypot(cenx,ceny)

            #center
            length_c=math.hypot(q2-x1,p2-y1)
            length1_th = math.hypot(cx - u1, cy - v1)
            length1_c = math.hypot(q2 - u1, p2 - v1)
            length2_c = math.hypot(q2 - w1, p2 - k1)
            length3_c = math.hypot(q2 - z1, p2 - r1)

            # Want
            length_w = math.hypot(u1 - x1, v1 - y1)
            length1_w = math.hypot(w1 - u1, k1 - v1)
            length2_w = math.hypot(z1 - w1, r1 - k1)
            length3_w = math.hypot(m1 - z1, n1 - r1)

            #Hand to the center
            length_center = math.hypot(cenx - lmList[0][1], ceny - lmList[0][2])


            print(length3)
            # if length >= 80:
            #     cv2.putText(img, f'Good distance', (200, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            # if length>=80 and (length1<=50 and length2<=50 and length3<=50):
            #     cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #     cv2.putText(img, f'One', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            #
            # if length>=80 and (length1>=80 and length2<=50 and length3<=50):
            #     cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #     cv2.putText(img, f'Two', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            #
            # if length>=80 and (length1>=80 and length2>=80 and length3<=50):
            #     cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #     cv2.putText(img, f'Three', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            #
            # if length>=80 and (length1>=80 and length2>=80 and length3>=50):
            #     cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #     cv2.putText(img, f'Four', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            if length_center<220:
                cv2.putText(img, f'Accuracy:Low', (400, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            else:
                cv2.putText(img, f'Accuracy:High', (400, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)



            if length>=80 and (length1<=50 and length2<=50 and length3>=50 and length4>=40):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'ILY', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("I love you")

            if length>=80 and (length1<=50 and length2<=50 and length3>=50 and length4<=40):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'YOO', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("YO")

            if length_c>=200 and (length1_c>=200 and length2_c>=200 and length3_c>=150 and length4>=40):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Hi!!', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("Hi")

            if length<=70 and (length1<=70 and length2<=70 and length3<=70 and length4>=80):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Good Job', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("Good Job")
            # if length_c<=100 and (length1_c<=100 and length2<=100 and length3_c<=100 and length4>=40):
            #     cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            #     cv2.putText(img, f'Want?', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

            if length_w<=70 and (length1_w<=70 and length1_c<=150 and length3<=30 and length4<=65):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'Want?', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("Want")

            if length <= 50 and (length1 <= 50 and length2 <= 50 and length3 >= 100 and length4 <= 50):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'I', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("I")

            if length>=80 and (length1>=80 and length2<=50 and length3<=50):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'You', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("You")

            if length>=80 and (length1<=50 and length2<=50 and length3<=50):
                cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                cv2.putText(img, f'COME  HERE', (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                #ts.text_to_speech("COME  HERE")



        cTime =time.time()
        fps =1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
        cv2.imshow("Img",img)
        cv2.waitKey(1)