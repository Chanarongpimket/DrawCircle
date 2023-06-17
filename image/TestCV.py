import cv2 as cv

img = cv.imread('image/1.jpeg')

print('Data type of image (OpenCV):', type(img))

cv.imshow('Ex1', img)

# cv.imwrite('out.png', img)

cv.waitKey(delay=5000)

cv.destroyAllWindows()





