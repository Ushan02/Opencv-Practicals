import cv2
import numpy as np

frame=cv2.imread('images/plants/D5.png')

height,width=frame.shape[0:2]
frame=cv2.resize(frame,(int(width/2),int(height/2)))

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_color = np.array([25,40,55])
upper_color = np.array([95,255,255])

mask = cv2.inRange(hsv, lower_color, upper_color)
res = cv2.bitwise_and(frame,frame, mask=mask)

contours, hierarchy = cv2.findContours(
    mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE
)

print('no. contours:',len(contours))

for cnt in contours:
    area=cv2.contourArea(cnt)
    print(area)

    if(area>150):
        cv2.drawContours(frame, [cnt], -1, (0,255,255), 1)

        x,y,w,h = cv2.boundingRect(cnt)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.circle(frame,(int(x+w/2),y),5,(0,0,255),-1)
        cv2.circle(frame,(int(x+w/2),y+h),5,(0,0,255),-1)

        cv2.putText(frame,"Height:"+str(h),(x+w,y+h),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv2.imshow('frame',frame)


k = cv2.waitKey(0)
cv2.destroyAllWindows()
