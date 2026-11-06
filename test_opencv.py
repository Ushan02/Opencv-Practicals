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
#find contours

img =cv2.imread('images/gray_image.png')
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imggray,80,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:
    area=cv2.contourArea(cnt)
    print(area)

    if(area>1000 and area<5000):
        cv2.drawContours(img, [cnt], -1, (0,255,0), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


cv2.imshow('thresh',thresh)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#This code reads a image, converts it into grayscale, and applies thresholding to create a binary image. It then detects all object boundaries (contours) using `cv2.findContours()` and prints the total number of contours and the number of points in the first contour. Finally, it draws all detected contours in green on the original image and displays both the binary image and the image with highlighted contours.

