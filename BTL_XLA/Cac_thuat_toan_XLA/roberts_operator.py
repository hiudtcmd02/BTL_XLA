from PIL import Image
import numpy as np

def roberts_operator(image):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = image.convert("L")

    # Chuyển đổi ảnh thành mảng numpy
    image_array = np.array(grayscale_image)

    # Ma trận lọc Roberts Gx
    filter_matrix_gx = np.array([[1, 0], [0, -1]])

    # Ma trận lọc Roberts Gy
    filter_matrix_gy = np.array([[0, 1], [-1, 0]])

    # Áp dụng ma trận lọc Gx và Gy lên ảnh
    filtered_image_gx = np.abs(np.convolve(image_array, filter_matrix_gx, mode="same"))
    filtered_image_gy = np.abs(np.convolve(image_array, filter_matrix_gy, mode="same"))

    # Kết hợp hai ảnh kết quả
    combined_image = np.sqrt(np.square(filtered_image_gx) + np.square(filtered_image_gy))

    # Chuyển đổi lại thành ảnh PIL
    edge_image = Image.fromarray(combined_image.astype(np.uint8))

    return edge_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.png"

# Đọc ảnh
image = Image.open(image_path)

# Áp dụng thuật toán Toán tử Roberts
edge_result = roberts_operator(image)

# Lưu ảnh kết quả
output_path = "path/to/save/edge_image.png"
edge_result.save(output_path)

# Hiển thị ảnh kết quả
edge_result.show()