import cv2 as cv

img = cv.imread('week3/pic/market.JPG',cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1,0,ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0,1,ksize=5)

print('input type :',img.dtype)
print('Laplacian type :',laplacian)
print('Sobel X type: ',sobelx.dtype)
print('Sobel Y type: ',sobely.dtype)

cv.imwrite('laplacian.png',laplacian)
cv.imwrite('sobel x.png',sobelx)
cv.imwrite('sobel y.png',sobely)