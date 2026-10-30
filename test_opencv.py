import cv2
import cv2 as cv

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

source=cv.VideoCapture(0) #for web cam'''


#this code use for open and play video file, it reads the video frame by frame and display each frame in window.
#the video stop automatically whhen it  end or user press ESC

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



