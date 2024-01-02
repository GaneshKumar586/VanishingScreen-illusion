import cv2
# import os
vid = cv2.VideoCapture(0)
while True:
    suc, img = vid.read()
    if not suc:
        print('Couldn\'t capture the video check the settings')
        break
    cv2.imshow("image", img)
    # print('e')
    if cv2.waitKey(6) == ord('q'):
        cv2.imwrite('IllusionBackground.jpg',img)
        break

vid.release()
cv2.destroyAllWindows()
