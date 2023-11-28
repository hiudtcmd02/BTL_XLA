import cv2
import numpy as np

def laplacian_operator(image):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng ma trận lọc Laplacian
    laplacian_image = cv2.Laplacian(grayscale_image, cv2.CV_64F)

    # Chuẩn hóa độ sáng của ảnh
    laplacian_image = cv2.normalize(laplacian_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return laplacian_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.jpg"

# Đọc ảnh
image = cv2.imread(image_path)

# Áp dụng thuật toán Toán tử Laplacian
laplacian_result = laplacian_operator(image)

# Hiển thị ảnh kết quả
cv2.imshow("Laplacian Image", laplacian_result)
cv2.waitKey(0)
cv2.destroyAllWindows()