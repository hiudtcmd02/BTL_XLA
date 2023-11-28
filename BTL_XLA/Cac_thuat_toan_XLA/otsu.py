import cv2

def otsu_thresholding(image):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng phân ngưỡng Otsu
    _, thresholded_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.jpg"

# Đọc ảnh
image = cv2.imread(image_path)

# Áp dụng thuật toán Otsu
otsu_result = otsu_thresholding(image)

# Hiển thị ảnh kết quả
cv2.imshow("Otsu Thresholding", otsu_result)
cv2.waitKey(0)
cv2.destroyAllWindows()