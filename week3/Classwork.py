import cv2 as cv
import random

img = cv.imread('week3/pic/p1.jpg',cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 255

number_of_black_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0

# cv.imwrite('img1.pg',img)
cv.imshow('img1',img)
cv.waitKey(0)
cv.destroyAllWindows()