import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
from cvzone.FPS import FPS

cap = cv2.VideoCapture(0)
cap.set(3, 648)
cap.set(4, 488)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fpsReader = FPS()

listImg = os.listdir("Images")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f"Images/{imgPath}")
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[indexImg], cutThreshold=0.98)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)

    fps, imgStacked = fpsReader.update(imgStacked)

    print(indexImg)
    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('b'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('n'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    if key == ord('q'):
        break