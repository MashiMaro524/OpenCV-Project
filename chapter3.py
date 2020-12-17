import cv2 # cv stands for computer vision
import numpy as np

#in cv2, height is downwards positve

img = cv2.imread("pengu.png")
print(img.shape) # results : (height,width,channel{3 = bgr})

imgResize = cv2.resize(img,(300,300)) # cv2.resize(image to resize , (width,height))

imgCropped = img[0:200,50:150] #img[height lower :upper limits,width lower : upper limits]

cv2.imshow("Image",img)
cv2.imshow("Image Resized",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)