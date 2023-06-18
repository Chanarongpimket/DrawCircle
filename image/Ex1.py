import cv2 as cv

img = cv.imread('image/1.jpeg')

print('Data type of image (OpenCV):', type(img))

cv.imshow('Ex1', img) # แสดงภาพ

cv.waitKey(delay=3000) # รอเวลา destroy

cv.destroyAllWindows() # ปิดหน้าต่างทั้งหมด

# cv.imwrite('out.png', img)
# cv.resize(img,(400,400))



