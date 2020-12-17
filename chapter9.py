import cv2
import numpy as np
width =480
height =640
##cv2.CascadeClassifier(xml file location)q
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread('lena.png')
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

##faceCascade.detectMultiScale(img to detect,scale,min. neighbours to scan)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # declare the first 4 points from the image (find the values from paint)
    pts1 = np.float32([[478, 134], [664, 87], [614, 339], [818, 284]])

    # declare the 4 points from to be warped to
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # cv2.getPerspectiveTransform(matrix to be warped,matrix to be warped to)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

cv2.imshow('Result',img)
cv2.waitKey(0)