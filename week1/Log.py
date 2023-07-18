import cv2 as cv
import numpy as np

img_in = cv.imread('week1/pic/room.jpg', cv.IMREAD_GRAYSCALE)

for param in range(1, 5):
    img_out = np.log(img_in + param)
    img_max = np.max(img_out)
    img_out = img_out * (255 / img_max)
    img_out = np.array(img_out, dtype='uint8')
    
    cv.imshow(f'Log Image Out (param={param})', img_out)
    cv.waitKey(2000)

cv.destroyAllWindows()

# import cv2 as cv
# import numpy as np

# img_in = cv.imread('work1/pic/room.jpg',cv.IMREAD_GRAYSCALE)

# img_out = np.log(img_in) #ปรับระดับ Intensity Level ของภาพโดยใช Log มืด -> สว่าง

# img_max = np.max(img_out)
# img_out = img_out * ( 255 / img_max )

# img_out = np.array(img_out,dtype='uint8')

# cv.imshow('Log Image In',img_in)
# cv.imshow('Log Image Out',img_out)
# cv.waitKey(delay=2000)
# cv.destroyAllWindows()

# cv.imwrite('Input.png',img_in)
# cv.imwrite('Output.png',img_out)
