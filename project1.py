import cv2 # cv stands for computer vision
import numpy as np

##Using webcam
cap = cv2.VideoCapture(0) # integers of 0,1 correspond to your installed webcams
#cap.set(id-coresponds-to-its-specifications,amount)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100)#brightnesqqs
#as video is a sequence of images , while loop is used

##Array in the sequence of :
##Hue Min,Saturation Min,Values Min,Hue Max,Saturation Max,Values Max,
myColors = [[89,84,0,179,255,255],
            [35,82,0,179,76,255]]


#colour values in the format of BGR
myColorValues = [[233,50,12],
                 [12,233,23]]
myPoints = []##[x,y,colorId]


def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])  # lower boundary matrix
        upper = np.array(color[3:6])  # upper boundary matrix
        # changed image = cv2.inRange(image to use,lower boundary matrix of (hue,sat,value),upper boundary matrix of (hue,sat,value))
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
            count+=1
        cv2.imshow(str(color[0]),mask)
        return newPoints

def getContours(img):
    ##cv2.findContours(image to find Contours,retrieval method,approximation)
    ##cv2.RETR_EXTERNAL - obtain the extreme outer contours
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        ##cv2.contourArea(cnt to be found) - to find the area of the contour
        area =cv2.contourArea(cnt)
        ##cv2.drawContours(image to draw,contour to draw,index{-1 represents all},(colour code),thickness)
        if area>800:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            ##cv2.arcLength(contour to measure,Boolean of is it closed or not) -calculates the arc length
            peri =cv2.arcLength(cnt,True)
            ##cv2.approxPolyDP(contour to approx,resolution,Boolean whether is it closed)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
        return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

while True:
# "success" show whether the reading is successful or not, while "img" is the variable that the image has read into
# "success" will be a boolean
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Video",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #when you press "q" ,the loop breaks
        break