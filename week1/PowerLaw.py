import cv2 as cv
import numpy as np

img_in = cv.imread('week1/pic/Sea.jpg', cv.IMREAD_GRAYSCALE)

for gamma in range(1, 5):
    gamma_corrected = (img_in / 255) ** gamma
    gamma_corrected = gamma_corrected * 255
    img_out = np.array(gamma_corrected, dtype='uint8')
    cv.imshow(f'Power-LawOUT (gamma={gamma})', img_out)
    cv.waitKey(2000)
    # cv.imwrite(f'OutputPowerLaw_gamma_{str(gamma)}.png', img_out)
    # สว่าง -> มืด

cv.destroyAllWindows()