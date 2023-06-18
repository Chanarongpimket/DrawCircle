import cv2 as cv

img = cv.imread('image/2.jpeg',0) # เพิ่ม 0 เป็นการเปลี่นโหมด Gray mode

print('Data type : ',type(img))
print('No of Dimention : ',img.ndim)
print('Size of each dimension : ',img.shape)

# cv.namedWindow('hel',cv.WINDOW_NORMAL) #หน้าต่างที่สามารถปรับขนาดได้ นั่นคือผู้ใช้สามารถเปลี่ยนขนาดหน้าต่างได้ตามความต้องการ
cv.imshow('hel',img)
cv.waitKey(0)
cv.destroyAllWindows()