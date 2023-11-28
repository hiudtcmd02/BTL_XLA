from PIL import Image

def histogram_equalization(image):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = image.convert("L")

    # Tính toán histogram
    histogram = grayscale_image.histogram()

    # Tính toán histogram tích lũy
    cumulative_histogram = [sum(histogram[:i+1]) for i in range(len(histogram))]

    # Chuẩn hóa histogram tích lũy
    normalized_histogram = [c * 255 / cumulative_histogram[-1] for c in cumulative_histogram]

    # Tạo bản đồ tương ứng
    mapping = [round(value) for value in normalized_histogram]

    # Tạo ảnh mới với giá trị pixel đã cập nhật
    equalized_image = grayscale_image.point(mapping)

    return equalized_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.png"

# Đọc ảnh
image = Image.open(image_path)

# Áp dụng thuật toán Cân bằng lược đồ xám
equalized_result = histogram_equalization(image)

# Lưu ảnh kết quả
output_path = "path/to/save/equalized_image.png"
equalized_result.save(output_path)

# Hiển thị ảnh kết quả
equalized_result.show()