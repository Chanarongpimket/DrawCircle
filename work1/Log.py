import cv2 as cv
import numpy as np

img_in = cv.imread('work1/pic/dark.jpg',cv.IMREAD_GRAYSCALE)

img_out = np.log(img_in)

img_max = np.max(img_out)
img_out = img_out * ( 255 / img_max )

img_out = np.array(img_out,dtype='uint8')

cv.imshow('Log Image In',img_in)
cv.imshow('Log Image Out',img_out)
cv.waitKey(delay=10000)
cv.destroyAllWindows()
# cv.imwrite('Input.png',img_in)
# cv.imwrite('Output.png',img_out)