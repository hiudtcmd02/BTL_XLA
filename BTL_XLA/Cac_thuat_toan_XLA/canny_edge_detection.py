import cv2

def canny_edge_detection(image, threshold1, threshold2):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Làm mờ ảnh bằng bộ lọc Gaussian
    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Áp dụng phương pháp Canny
    edges = cv2.Canny(blurred_image, threshold1, threshold2)

    return edges

# Đường dẫn đến ảnh
image_path = "path/to/your/image.jpg"

# Đọc ảnh
image = cv2.imread(image_path)

# Áp dụng thuật toán Canny Edge Detection
canny_result = canny_edge_detection(image, 100, 200)

# Hiển thị ảnh kết quả
cv2.imshow("Canny Edge Detection", canny_result)
cv2.waitKey(0)
cv2.destroyAllWindows()