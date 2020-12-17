import cv2 # cv stands for computer vision


##############################################
frameWidth = 640
frameHeight =480
nPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,255)
##############################################


cap = cv2.VideoCapture(0) # integers of 0,1 correspond to your installed webcams
##cap.set(id-coresponds-to-its-specifications,amount)
cap.set(3,640) #width
cap.set(4,480) #height
cap.set(10,100)#brightness
count = 0

#as video is a sequence of images , while loop is used
while True:
     # "success" show whether the reading is successful or not, while "img" is the variable that the image has read into
     # "success" will be a boolean
     success,img = cap.read()
     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     ##faceCascade.detectMultiScale(img to detect,scale,min. neighbours to scan)
     numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

     for (x, y, w, h) in numberPlates:
         area = w*h
         if area>minArea :
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Number Plate",(x,y-5),
                     cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
     cv2.imshow('Result', img)
     if cv2.waitKey(1)& 0xFF == ord("s"):
         cv2.imwrite("Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
         cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
         cv2.putText(img,"Scan Saved",(150,255),cv2.FONT_HERSHEY_DUPLEX,
                     2,(0,0,255),2)
         cv2.imshow("Result",img)
         cv2.waitKey(500)
         count+=1


