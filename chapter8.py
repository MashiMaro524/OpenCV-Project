import cv2
import numpy as np

##############################################################
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
##############################################################

def getContours(img):
    ##cv2.findContours(image to find Contours,retrieval method,approximation)
    ##cv2.RETR_EXTERNAL - obtain the extreme outer contours
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        ##cv2.contourArea(cnt to be found) - to find the area of the contour
        area =cv2.contourArea(cnt)
        #print(area)
        ##cv2.drawContours(image to draw,contour to draw,index{-1 represents all},(colour code),thickness)
        if area>500:
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            ##cv2.arcLength(contour to measure,Boolean of is it closed or not) -calculates the arc length
            peri =cv2.arcLength(cnt,True)
            #print(peri)
            ##cv2.approxPolyDP(contour to approx,resolution,Boolean whether is it closed)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx)) #gives the number of the cornerpoints
            objCor = len(approx)
            ##cv2.boundingRect(approx from cv2.approxPolyDP)
            ##gives the x,y coord and the width , height
            x,y,w,h = cv2.boundingRect(approx)
            if objCor == 3: objectType = "Triangle"
            elif objCor == 9: objectType = "Heart"
            elif objCor == 4:
                #check either is square or rectangle
                aspRatio =w/float(h)
                if aspRatio >0.95 and aspRatio <1.05:objectType="Square"
                else :objectType="Rectangle"
            elif objCor==8:
                aspRatio = w / float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Circle"
                else:
                    objectType = "Oval"
            else:objectType="None"
            #cv2.rectangle(imgContour,(x,y-coord of retangle),(width,height),(color values),thickness)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            #cv2.putText(image to put text,text to print,position to print,
            # font type,scale of text,colour values,scale of text)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)


path = 'shapes_v2.png'
img =cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor (img,cv2.COLOR_BGR2GRAY)
#cv2.GaussianBlur(img to blur,(kernel size),sigma value-degree of blur)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)
imgStack =stackImages(0.8,([img,imgGray,imgBlur],
                           [imgCanny,imgContour,imgBlank]))

cv2.imshow("Image Stacked",imgStack)

cv2.waitKey(0)