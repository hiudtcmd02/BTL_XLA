import cv2
import numpy as np

# Đọc hình ảnh gốc
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Xác định kernel hoặc structuring element
kernel = np.ones((3, 3), np.uint8)

# Áp dụng phép giãn hình
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Hiển thị hình ảnh gốc và hình ảnh đã được giãn hình
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()