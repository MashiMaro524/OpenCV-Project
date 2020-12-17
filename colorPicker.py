import cv2 # cv stands for computer vision
import numpy as np

##Using webcam
cap = cv2.VideoCapture(0) # integers of 0,1 correspond to your installed webcams
#cap.set(id-coresponds-to-its-specifications,amount)
cap.set(3,320) #width
cap.set(4,240) #height
cap.set(10,100)#brightness
#as video is a sequence of images , while loop is used

def empty(a):
    pass

#cv2.namedWindow("Name of Window")
cv2.namedWindow("TrackBars")
#cv2.resizeWindow("Name of Window",height,width)
cv2.resizeWindow("TrackBars",640,240)
#cv2.createTrackbar("Name of Trackbar","Name of Window",min value,max value,function to pass)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Value Min","TrackBars",0,255,empty)
cv2.createTrackbar("Value Max","TrackBars",255,255,empty)

while True:
# "success" show whether the reading is successful or not, while "img" is the variable that the image has read into
# "success" will be a boolean
    _,img = cap.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])  # lower boundary matrix
    upper = np.array([h_max, s_max, v_max])  # upper boundary matrix
    # changed image = cv2.inRange(image to use,lower boundary matrix of (hue,sat,value),upper boundary matrix of (hue,sat,value))
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])
    cv2.imshow("img",hStack)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #when you press "q" ,the loop breaks
        break


cap.release()
cv2.destroyAllWindows()