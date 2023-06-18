import numpy as np
import cv2 as cv

img = np.zeros([200,300],dtype=np.uint8)

for y in range(75,125):
    for x in range(50,250):
        img[y,x] = 255

cv.imshow('Output',img)
cv.waitKey(delay=5000)
cv.destroyAllWindows