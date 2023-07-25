import cv2 as cv

img = cv.imread('week2/pic/cat.jpg',cv.IMREAD_GRAYSCALE)

# laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1,0,ksize=5)
# sobely = cv.Sobel(img, cv.CV_64F, 0,1,ksize=5)

print('input type :',img.dtype)
# print('Laplacian type :',laplacian)
print('Sobel X type: ',sobelx.dtype)
# print('Sobel Y type: ',sobely.dtype)

# laplacian = cv.normalize(laplacian, None,0,255,cv.NORM_MINMAX,cv.CV_8U)
sobelx = cv.normalize(sobelx,None,0,255,cv.NORM_MINMAX,cv.CV_8U)
# sobely = cv.normalize(sobely,None,0,255,cv.NORM_MINMAX,cv.CV_8U)

# cv.imshow('laplacian.png',laplacian)
cv.imwrite('sobel cat.png',sobelx)
# cv.imshow('sobel y.png',sobely)


cv.waitKey(0)
cv.destroyAllWindows()