import cv2
import numpy as np

#small example about 3-D matrix
img2 = np.zeros((3,2,4),np.uint8) #declaring a zero matrix with size specified
img2[2,1,1]=510
print(img2)

#np.uint8 - gives values from 0 - 255
img = np.zeros((512,512,3),np.uint8) #declaring a zero matrix with size specified
#print(img)

#img[:]=255,0,0 #the whole screen is blue
#img[100:200,200:300]=0,0,510 #shows a blue square

#cv2.line(img to draw ,(starting point),(ending point), (colour values),thickness)
#cv2.line(img,(0,0),(300,300),(0,255,0),3)

#img.shape[0] -> height
#img.shape[1] -> width

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#cv2.rectangle(img to draw ,(upper left corner point),(lower right corner point), (colour values),thickness)
# change thickness to cv2.FILLED {if you want to fill the rectangle}
cv2.rectangle(img,(0,0),(250,350),(255,0,0),2)

#cv2.circle(img to draw,(centre point),radius,(colour values),thickness))
cv2.circle(img,(400,50),30,(255,255,0),5)

#cv2.putText(img to use," Text ",(origin point),cv2.FONT_(Desired Font),scale,(color code),thickness)
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("Image",img)


cv2.waitKey(0)