import cv2 as cv
import numpy as np

img_in = cv.imread('work1/pic/light.jpg',cv.IMREAD_GRAYSCALE)

gamma = 2
gamma_corrected = (img_in/255)**gamma

gamma_corrected = gamma_corrected**255

img_out = np.array(gamma_corrected,dtype='uint8')

cv.imshow('Power-LawIn',img_in)
cv.imshow('Power-LawOUT',img_out)
cv.waitKey(delay=10000)
cv.destroyAllWindows()

# cv.imwrite('InputPowerLaw.png',img_in)
# cv.imwrite('OutputPowerLaw.png',img_out)