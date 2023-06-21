import numpy as np
import cv2 as cv

img = np.zeros([1000,1000],dtype=np.uint8)

cv.circle(img,(150,150),100,(255,255,255),-1)

cv.circle(img,(500,500),300,(255,255,255),10)
cv.circle(img,(500,500),200,(255,255,255),2)
cv.circle(img,(500,500),100,(255,255,255),2)

cv.circle(img,(980,880),200,(255,255,255),-1)


cv.imshow('Output',img)
cv.waitKey(delay=5000)
cv.destroyAllWindows