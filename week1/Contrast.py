import cv2 as cv
import numpy as np

def pixelVal(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1)*pix
    elif ( r1 < pix and pix <= r2):
        return ((s2 - s1)/(r2 -r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255-r2)) * (pix - r2) + s2

img = cv.imread('week1/pic/Sea.jpg', cv.IMREAD_GRAYSCALE)

r1 = 100
s1 = 0
r2 = 250
s2 = 256

pixelVal_vec = np.vectorize(pixelVal)

contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

cv.imshow('Contrast Stretched Image', contrast_stretched)
cv.waitKey(3000)
cv.destroyAllWindows()