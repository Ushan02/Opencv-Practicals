import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

frame=cv2.imread('images/plants/D12.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_color = np.array((22,50,134))
upper_color = np.array((80,255,255))

mask=cv2.inRange(hsv, lower_color, upper_color)

res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('HSV',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()