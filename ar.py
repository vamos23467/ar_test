#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

img1 = cv2.imread("test-img01.png")

def ConvImg(corners, i, img, convimg):
    x = int(corners[i][0][0][0])
    y = int(corners[i][0][0][1])
    w = int(corners[i][0][2][0]) - x
    h = int(corners[i][0][2][1]) - y
    
    if w > 0 and h > 0:
        convimg = cv2.resize(convimg, (w, h))
        img[y:y+h, x:x+w] = convimg
    
    return img

def arReader():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        Height, Width = frame.shape[:2]
        img = cv2.resize(frame, (Width, Height))

        corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary)

        if corners and ids is not None and len(ids) > 0:
            text1 = "detected"
        else:
            text1 = "None"

        cv2.putText(img,
                    text=text1,
                    org=(100, 300),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.0,
                    color=(0, 255, 0),
                    thickness=2,
                    lineType=cv2.LINE_4)

        cv2.imshow('drawDetectedMarkers', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

arReader()
