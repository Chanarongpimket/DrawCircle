import cv2
import numpy as np

# อ่านภาพเข้ามาและแปลงเป็นรูปแบบของ grayscale
image = cv2.imread("week2/pic/Circle Objects.png",cv2.IMREAD_GRAYSCALE)

# ลบ noise ในภาพโดยใช้ฟิลเตอร์ Gaussian
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# ค้นหาวงกลมโดยใช้ cv2.HoughCircles()
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=100)

# แปลงตำแหน่งและรัศมีของวงกลมให้อยู่ในรูปแบบของจำนวนเต็ม
circles = np.uint16(np.around(circles))

# วาดวงกลมลงบนภาพ
for circle in circles[0, :]:
    center = (circle[0], circle[1])
    radius = circle[2]
    intensity = int(blurred[circle[1], circle[0]])
    cv2.circle(image, center, radius, (0, 0, intensity), 2)

# แสดงผลลัพธ์ภาพ
cv2.imshow("Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
