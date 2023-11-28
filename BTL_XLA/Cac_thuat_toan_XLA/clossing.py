import cv2
import numpy as np

# Đọc hình ảnh gốc
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Xác định kernel hoặc structuring element
kernel = np.ones((3, 3), np.uint8)

# Áp dụng phép đóng - closing
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Hiển thị hình ảnh gốc và hình ảnh đã được đóng - closing
cv2.imshow("Original Image", image)
cv2.imshow("Closed Image", closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()