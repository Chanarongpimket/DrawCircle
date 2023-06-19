import numpy as np
import cv2 as cv

img = np.zeros([500,500],dtype=np.uint8)

cv.line(img,(50,50),(400,400),(255,255,255),(5)) # รูป , pt1 , pt2 , BGR , size
cv.line(img,(50,400),(400,50),(255,255,255),(5)) # รูป , pt1 , pt2 , BGR , size

cv.imshow('Output',img)
cv.waitKey(delay=5000)
cv.destroyAllWindows