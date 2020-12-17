import cv2
import numpy as np

img = cv2.imread("poker.jpg")

width,height = 250,350 # declaring the values

#declare the first 4 points from the image (find the values from paint)
pts1 = np.float32([[478,134],[664,87],[614,339],[818,284]])

#declare the 4 points from to be warped to
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#cv2.getPerspectiveTransform(matrix to be warped,matrix to be warped to)
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#cv2.warpPerspective(img to be warped ,warped matrix,(width,height))
imgOutput= cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)