# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:30:18 2018

@author: Pc
"""

import cv2
import numpy as np
def main():
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
    while ret:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #Blue Color
        low=np.array([100,50,50])
        high=np.array([140,155,155])
        
        image_mask=cv2.inRange(hsv,low,high)
        output=cv2.bitwise_and(frame,frame,mask=image_mask)
        
        cv2.imshow("Image mask",image_mask)
        cv2.imshow("Webcam",frame)
        cv2.imshow("Output",output)
        
    # if ESC, exit
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
if "a"=="a":
    main()