import numpy as np
import cv2 as cv

img = cv.imread('week2/pic/Sea.JPG',0)

filterSize = 15
kernal = np.ones((filterSize,filterSize),np.float32)/(filterSize**2)

output = cv.filter2D(img, -1,kernal,borderType = cv.BORDER_REFLECT)

cv.imshow('filter', img)
cv.imshow('filterBlur', output)
cv.waitKey(0)

cv.destroyAllWindows()