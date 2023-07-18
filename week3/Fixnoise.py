import numpy as np
import cv2 as cv

img = cv.imread('week3/pic/img1.jpg',cv.IMREAD_GRAYSCALE)

output = cv.medianBlur(img,5)

test = output - img

cv.imshow('test1',output)
cv.waitKey(0)
cv.destroyAllWindows()