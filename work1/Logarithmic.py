import cv2 as cv
import numpy as np

img_in = cv.imread('work1/pic/room.jpg', cv.IMREAD_GRAYSCALE)

c = 255 / np.log(1+np.max(img_in))

log_img = c * (np.log(1 + img_in))

log_img = np.array(log_img,dtype = np.uint8)

cv.imshow('Log Image out',img_in)
cv.waitKey(delay=3000)
cv.destroyAllWindows()
