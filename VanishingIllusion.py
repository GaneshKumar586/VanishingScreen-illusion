import cv2
import os
vid = cv2.VideoCapture(0)
import numpy as np

BackgroundImg = cv2.imread('./IllusionBackground.jpg')
# BackgroundImg = cv2.imread('./bg1.jpg')
# greenmatCurr = cv2.imread('./greenmatCurr.jpg')
# print(greenmatCurr.shape)
# greenmatPrev = cv2.imread('./greenmatPrev.jpg')
# # greenmatPrev.resize(greenmatPrev, (252, 655, 3))
# print(greenmatPrev.shape)
# cv2.imshow("background", BackgroundImg)
try:
    while True:
        suc, img = vid.read()
        # x = cv2.imread('./bg1.jpg')
        # x = cv2.imread(img)
        # print(img.shape)
        # img = greenmatCurr
        # BackgroundImg = greenmatPrev
        if not suc:
            print('Couldn\'t capture the video check the settings')
            break
        if not os.path.exists( './IllusionBackground.jpg' ):
            break

        hsvImg = cv2.cvtColor(img , cv2.COLOR_BGR2HSV )
        sheetColorLow = np.array([30, 0, 90])
        sheetColorHigh = np.array([50,255, 255])
        range1 = cv2.inRange(hsvImg, sheetColorLow, sheetColorHigh )

        sheetColorLow = np.array([50, 0, 50])
        sheetColorHigh = np.array( [80, 255, 255])
        range2 = cv2.inRange(hsvImg, sheetColorLow, sheetColorHigh )

        range = range1 + range2
        range = cv2.morphologyEx(range, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations =10)
        range = cv2.morphologyEx(range, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
        range3 = cv2.bitwise_not(range)
        removedPartImg = cv2.bitwise_and( BackgroundImg , BackgroundImg, mask = range)
        remainingPartImg = cv2.bitwise_and( img , img, mask = range3)

        cv2.imshow("IllusionImage", removedPartImg + remainingPartImg)
        cv2.waitKey(1)

except KeyboardInterrupt:
    print('Video capture ended by KeyBoardInterrupt')

finally:
    vid.release()
    cv2.destroyAllWindows()