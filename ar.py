# import cv2
# import numpy as np

# aruco = cv2.aruco
# dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
# SIZE = 150
# ImgList1 = []
# ImgList2 = []
# WiteList = []
# def arGenerator():
#     img_white = np.ones((SIZE,SIZE, 3),np.uint8)*255
#     for i in range(1,6):
#         fileName = "ar_" + str(i) + ".png"
#         generator = cv2.drawFrameAxes(dictionary, i, SIZE)
#         cv2.imwrite(fileName, generator)
#         ImgList1.append(cv2.imread(fileName))
#         ImgList1.append(img_white)
#         WiteList.append(img_white)
#         WiteList.append(img_white)
#         convImg1 = cv2.hconcat(ImgList1)
#         convWhite = cv2.hconcat(WiteList)
#     for i in range(6,11):
#         fileName = "ar_" + str(i) + ".png"
#         generator = aruco.drawMarker(dictionary, i, SIZE)
#         cv2.imwrite(fileName, generator)
#         ImgList2.append(cv2.imread(fileName))
#         ImgList2.append(img_white)
#         convImg2 = cv2.hconcat(ImgList2)
#     TestList = [convImg1, convWhite, convImg2]
#     convImg3 = cv2.vconcat(TestList)
#     cv2.imshow('ArMarker1',convImg3)
#     cv2.imwrite("Result.jpg", convImg3)
#     cv2.waitKey(0)

# arGenerator()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time
aruco = cv2.aruco #arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

img1 = cv2.imread("test-img01.png")
text1 = ""
# img2 = cv2.imread("hamstar.png")
# img3 = cv2.imread("mogura.png")

def ConvImg(corners, i, img, convimg):
    x=int(corners[i][0][0][0])
    y=int(corners[i][0][0][1])
    w=int(corners[i][0][2][0]) - int(corners[i][0][0][0])
    h=int(corners[i][0][2][1]) - int(corners[i][0][0][1])
    if w > 0 and h > 0:
        convimg = cv2.resize(convimg,(w,h))
        img[y:y+h,x:x+w] = convimg
    return img

def arReader():
    cap = cv2.VideoCapture(0) #ビデオキャプチャの開始
    while True:
        ret, frame = cap.read() #ビデオキャプチャから画像を取得

        Height, Width = frame.shape[:2] #sizeを取得
        img = cv2.resize(frame,(int(Width),int(Height)))

        corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出
        #aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する

        try:
            if corners != [] and len(ids) > 0:
                text1 = "detected"
            else:
                text1 = "None"
                # for i in range(len(ids)):
                #     if ids[i] == 10:
                #         print("detected")

                #     #if ids[i] == 5:
                #         #img = ConvImg(corners, i, img, img2)
                #     #if ids[i] == 3:
                #         #img = ConvImg(corners, i, img, img3)
            #time.sleep(30)
        except:
            #time.sleep(30)
            text1 = "error"
        cv2.putText(img,
            text=text1,
            org=(100, 300),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_4)
        cv2.imshow('drawDetectedMarkers', img) #マーカが描画された画像を表示
        cv2.waitKey(1) #キーボード入力の受付

    cap.release() #ビデオキャプチャのメモリ解放
    cv2.destroyAllWindows() #すべてのウィンドウを閉じる


arReader()