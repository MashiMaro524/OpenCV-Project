#go to settings -> the porject file ->project intepreter and install the libraries
import cv2 # cv stands for computer vision
import numpy as np

##reading and displaying images
print("Package Imported")
img = cv2.imread("pengu.png") #read the image and specify the path of the image

kernel =np.ones((5,5),np.uint8) #define kernel for the dialation
#uint8->unsigned integers from 0 to 255

#cv2.cvtColor(name of the img variable,mode of color coversion) naming for color = BGR
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #change to gray color

#cv2.GaussianBlur(variable of img,kernel size(must be odd number matrix),sigmaX)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#cv2.Canny(name of image,threshold values,threshold values) #its a canny edge detector
imgCanny=cv2.Canny(img,100,100) #larger threshold values ->lesser edges

#cv2.dilate(name of img variable, the matrix , the movement/iterations)
imgDialation =cv2.dilate(imgCanny,kernel,iterations=1) #larger iterations ->thicker lines

#cv2.erode(name of img variable, the matrix , the movement/iterations)
imgEroded =cv2.erode(imgDialation,kernel,iterations=1)

#erode == opposite of dilation

cv2.imshow("Name of the directory",imgGray) #display the image {Arguements:(output{name of the directory},variable of image)}
cv2.imshow("Blurred image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0) #inside bracket in milliseconds # 0 means infinity

##reading and play video
# cap = cv2.VideoCapture("01-Introduction.mp4") #read the video into the variable
# #as video is a sequence of images , while loop is used
# while True:
#     # "success" show whether the reading is successful or not, while "img" is the variable that the image has read into
#     # "success" will be a boolean
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(30) & 0xFF ==ord('q'): #when you press "q" ,the loop breaks
#         break

# ##Using webcam
# cap = cv2.VideoCapture(0) # integers of 0,1 correspond to your installed webcams
# #cap.set(id-coresponds-to-its-specifications,amount)
# cap.set(3,640) #width
# cap.set(4,480) #height
# cap.set(10,100)#brightness
# #as video is a sequence of images , while loop is used
# while True:
#     # "success" show whether the reading is successful or not, while "img" is the variable that the image has read into
#     # "success" will be a boolean
#     success,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(30) & 0xFF ==ord('q'): #when you press "q" ,the loop breaks
#         break