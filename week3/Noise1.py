#Gaussian noise
import numpy as np
import cv2 as cv 

img = cv.imread('week3/pic/p1.jpg',cv.IMREAD_GRAYSCALE)

row = img.shape[0]
col = img.shape[1]
mean = 0
sigma = 30

noise = np.random.normal(mean,sigma,(row,col))

img = img + noise

img = cv.normalize(img, None,0,255, cv.NORM_MINMAX,cv.CV_8U)
noise = cv.normalize(noise,None,0,255,cv.NORM_MINMAX,cv.CV_8U)

cv.imshow('image with noise', img)
cv.imshow('only noise',noise)
cv.waitKey(0)
cv.destroyAllWindows()