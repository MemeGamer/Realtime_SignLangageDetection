import cv2
import numpy as np
import HandTrackingModule as htm
import math
from gtts import gTTS
import os
from playsound import playsound
import time
import TextToSpeech as ts
from datetime import datetime

#Fingers
Thumb=4
Index=8
Middle=12
Ring=16
Pinky=20
Wrist=0

#Declaration
TimeS=time.time()
Left=False
Right=False
wCam, hCam =640, 480
cenx=320
ceny=240
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
detector =htm.handDetector(detectionCon=0.7)
Detection= []
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img=detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    cv2.circle(img, (cenx,ceny), 5, (0, 0, 255), cv2.FILLED)
    if len(lmList)!=0:
        ts.text_to_speech("Hand")

    # Declare Points open the hand_landmarks.png
        P4_x, P4_y = lmList[4][1], lmList[4][2]
        P6_x, P6_y = lmList[6][1], lmList[6][2]

        P8_x,P8_y = lmList[8][1],lmList[8][2]
        P5_x, P5_y = lmList[5][1], lmList[5][2]

        P12_x,P12_y = lmList[12][1], lmList[12][2]
        P9_x,P9_y = lmList[9][1], lmList[9][2]

        P16_x,P16_y = lmList[16][1], lmList[16][2]
        P13_x,P13_y = lmList[13][1], lmList[13][2]

        P20_x, P20_y = lmList[20][1], lmList[20][2]
        P17_x, P17_y = lmList[17][1], lmList[17][2]


    #Center
        P0_x, P0_y = lmList[0][1], lmList[0][2]

        cv2.circle(img,(P8_x,P8_y),5,(255,0,255),cv2.FILLED)
        cv2.circle(img, (P5_x, P5_y), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img,(P8_x,P8_y),(P5_x,P5_y),(255,0,255),2)


    #Length Calculation
        P8_P5=math.hypot(P8_x-P5_x,P8_y-P5_y)
        P12_P9 = math.hypot(P12_x - P9_x,P12_y - P9_y)
        P16_P13 = math.hypot(P16_x - P13_x, P16_y - P13_y)
        P20_P17 = math.hypot(P20_x - P17_x, P20_y - P17_y)
        P4_P6 = math.hypot(P4_x - P6_x, P4_y - P6_y)
        P4_P8 = math.hypot(P4_x-P8_x,P4_y-P8_y)
        P12_P8 = math.hypot(P12_x-P8_x,P12_y-P8_y)


        P8_P0=math.hypot(P8_x-P0_x,P8_y-P0_y)
        P12_P0 = math.hypot(P12_x - P0_x,P12_y - P0_y)
        P16_P0 = math.hypot(P16_x - P0_x, P16_y - P0_y)
        P20_P0 = math.hypot(P20_x - P17_x, P20_y - P17_y)
        whatlen = math.hypot(cenx,ceny)



    #Hand to the center
        length_center = math.hypot(cenx - lmList[0][1], ceny - lmList[0][2])


    # Text Display
        def Text_display():
            for x in range(len(Detection)):
                cv2.putText(img, Detection[x], (130, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
                print(Detection[x])


        if length_center<250:
            cv2.putText(img, f'Accuracy:HIGH', (400, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        else:
            cv2.putText(img, f'Accuracy:LOW', (400, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)


    # Add Words Here
    #     if P8_P5>=80 and (P12_P9<=50 and P16_P13<=50 and P20_P17>=50 and P4_P6>=50):
    #         Detection = "ILY"
    #         Text_display()
    #
    #     if P8_P5>=80 and (P12_P9<=50 and P16_P13<=50 and P20_P17>=50 and P4_P6<=50):
    #         Detection = "YOO"
    #         Text_display()
    #         #ts.text_to_speech("YO")
    #
    #     if P8_P5<=70 and (P12_P9<=70 and P16_P13<=70 and P20_P17<=70 and P4_P6>=80):
    #         Detection = "GOOD JOB"
    #         Text_display()
    #         #ts.text_to_speech("Good Job")
    #
    #
    #     if P20_P0>=80 and (P8_P0<=80 and P12_P0<=80 and P16_P0<=80 and P4_P6<=50):
    #         Detection = "I"
    #         Text_display()
    #         #ts.text_to_speech("I")
    #
    #     if P8_P5>=80 and (P12_P9<=50 and P16_P13<=50 and P20_P17<=50 and P4_P6<=40 and P4_P8 >= 40):
    #         Detection="COME HERE"
    #         Text_display()
    #         #ts.text_to_speech("COME  HERE")
    #
    #     if P8_P0>=180 and (P12_P0>=180 and P16_P0>=180 and P20_P0>=80 and P4_P6>=80):
    #         Detection="HI"
    #         Text_display()

        if P4_P8 <= 40 and (P12_P9<=50 and P16_P13<=50 and P20_P17<=50):
                x = "Doing"
                if x not in Detection:
                    Detection.append(x)
                    Text_display()
                #ts.text_to_speech("Doing")

        if P8_P0>=180 and (P12_P0>=180 and P16_P0<=80 and P20_P0<=80 and P4_P6<=80 and P12_P8 >= 20):
            #Detection = "You"
            x = "You"
            if x not in Detection:
                Detection.append(x)
                Text_display()
            #Text_display()
        #
        if P12_P8 <= 20 and (P16_P0<=80 and P20_P0<=80 and P4_P6<=80):
                #Detection = "Are"
                x = "Are"
                if x not in Detection:
                    Detection.append(x)
                    Text_display()
                #Text_display()
        #
        if P8_P0>=180 and (P12_P0>=180 and P16_P0>=180 and P20_P0<=60):
                #Detection = "What"
                x = "What"
                if x not in Detection:
                    Detection.append(x)
                    Text_display()
                #Text_display()
        #
        # if P4_P8 <= 40 and (P12_P0>=180 and P16_P0>=180 and P20_P0>=80):
        #         Detection = "How are you"
        #         Text_display()

    cTime =time.time()
    fps =1/(cTime-pTime)
    pTime=cTime
    #print(cTime)
    # curr_time = datetime.now()
    # formatted_time = curr_time.strftime('%S')
    # print(formatted_time)
    cv2.putText(img,f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
    cv2.imshow("Img",img)
    cv2.waitKey(1)