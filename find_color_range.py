
import cv2
import numpy as np

#cap = cv2.VideoCapture(1)

def nothing(x):
    pass

cv2.namedWindow('result')

h,s,v = 100,100,100

cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

while(1):
    frame = cv2.imread('images/plants/D14.png')
    #ret,frame=cap.read()
    frame=cv2.resize(frame,(650,350))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')

    lower_color = np.array((h,s,v))
    upper_color = np.array((102, 255, 255))

    mask = cv2.inRange(hsv,lower_color, upper_color)
    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
