import cv2
import numpy as np

def sobel_operator(image):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng ma trận lọc Sobel
    sobel_x = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)

    # Kết hợp hai ảnh kết quả
    edge_image = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

    # Chuẩn hóa độ sáng của ảnh
    edge_image = cv2.normalize(edge_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return edge_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.jpg"

# Đọc ảnh
image = cv2.imread(image_path)

# Áp dụng thuật toán Toán tử Sobel
edge_result = sobel_operator(image)

# Hiển thị ảnh kết quả
cv2.imshow("Edge Image", edge_result)
cv2.waitKey(0)
cv2.destroyAllWindows()