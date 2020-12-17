import cv2
import numpy as np
############################################
widthImg = 640
heightImg  = 480
############################################
cap =cv2.VideoCapture(0)
cap.set(3,widthImg)
cap.set(4,heightImg)
cap.set(10,150)


def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny =cv2.Canny(imgBlur,200,200)
    kernel =  np.ones((5,5))
    imgDial =cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres =cv2.erode(imgDial,kernel,iterations=1)
    return imgThres


def getContours(img):
    biggest =np.array([])
    maxArea=0
    ##cv2.findContours(image to find Contours,retrieval method,approximation)
    ##cv2.RETR_EXTERNAL - obtain the extreme outer contours
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        ##cv2.contourArea(cnt to be found) - to find the area of the contour
        area =cv2.contourArea(cnt)
        #print(area)
        ##cv2.drawContours(image to draw,contour to draw,index{-1 represents all},(colour code),thickness)
        if area>5000:
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            ##cv2.arcLength(contour to measure,Boolean of is it closed or not) -calculates the arc length
            peri =cv2.arcLength(cnt,True)
            #print(peri)
            ##cv2.approxPolyDP(contour to approx,resolution,Boolean whether is it closed)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            if area>maxArea and len(approx)==4:
                biggest = approx
                maxArea = area
        cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    #print("add",add)
    myPointsNew[0]=myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1]=myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmin(diff)]
    #print("NewPoints",myPointsNew)
    return myPointsNew

def getWarp(img,biggest):
    biggest =reorder(biggest)
    # declare the first 4 points from the image (find the values from paint)
    pts1 = np.float32(biggest)
    # declare the 4 points from to be warped to
    # it will not work as the points will be vary but we have a structure
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    # cv2.getPerspectiveTransform(matrix to be warped,matrix to be warped to)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped

while True:
    success,img =cap.read()
    img = cv2.resize(img,(widthImg,heightImg))
    imgContour =img.copy()

    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    if biggest.size !=0:
        imgWarped =getWarp(img,biggest)
        imageArray = ([img,imgThres],
                     [imgContour,imgWarped])
    else :
        imageArray = ([img, imgThres],
                      [img, img])
    stackedImages = stackImages(0.6,imageArray)
    cv2.imshow("Result",stackedImages)
    #cv2.imshow("Image Warped", imgWarped)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break


