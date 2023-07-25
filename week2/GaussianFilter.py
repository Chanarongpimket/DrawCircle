import numpy as np
import cv2 as cv

img = cv.imread('week2/pic/Sea.JPG',cv.IMREAD_GRAYSCALE)

ksize = (31,31)
sigmaX = 5.0
output = cv.GaussianBlur(img,ksize,sigmaX,borderType=cv.BORDER_REFLECT)

cv.imshow('filter', img)
cv.imshow('filterBlur', output)
cv.waitKey(0)

cv.destroyAllWindows()