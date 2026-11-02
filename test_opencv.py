import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''img = cv.imread('images/flower.jpg')

if img is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    print("Image shape:", img.shape)
    print(type(img))


#change pixel color to black selected area
img[100:150,100:150]=[0,0,0]
cv.imshow("flower", img)
cv.waitKey(0)
cv.destroyAllWindows()

source=cv.VideoCapture(0) #for web cam


#this code use for open and play video file, it reads the video frame by frame and display each frame in window.
#the video stop automatically when it  end or user press ESC

source=cv.VideoCapture('dog_animation_20s.mp4')
while(True):
    ret,frame=source.read()
    if(ret==False):
        break
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if(key==27):
        break
cv2.destroyAllWindows()

#Color Conversion

img1=cv2.imread('images/flower.jpg',0) #gray
img2=cv2.imread('images/flower.jpg',1) #color
img3=cv2.imread('images/flower.jpg',2)

cv.imshow("flower1",img1)
cv.imshow("flower2",img2)
cv.imshow("flower3",img3)
cv.waitKey(0)
cv.destroyAllWindows()


#--------------------------------------------------------------#
#Image Thresholding

img=cv2.imread('images/flower.jpg',0)
#Binary inverse
ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
cv.imshow("flower1",thresh)
#Binary
ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
cv.imshow("flower2",thresh)

#To Zero (Keeps pixel values above 200 unchanged; changes the rest to zero.)
ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
cv.imshow("flower3",thresh)

#Truncate (Limits values greater than 200 to 200.)
ret,thresh=cv2.threshold(img,80,255,cv2.THRESH_TRUNC)
cv.imshow("flower4",thresh)

cv.waitKey(0)
cv2.destroyAllWindows()

#---------------------------------------------------------------#

#color segmentation


frame=cv2.imread('images/colors3.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_color = np.array((96,227,130))
upper_color = np.array((140,255,255))

mask=cv2.inRange(hsv, lower_color, upper_color)

res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('HSV',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

#This code reads an image and converts it from BGR to HSV colour space. It defines the lower and upper HSV colour ranges using NumPy arrays and detects the selected colour using inRange. Then, using bitwise_and  extracts the detected colour from the original image.

#-----------------------------------------------------------#
'''

