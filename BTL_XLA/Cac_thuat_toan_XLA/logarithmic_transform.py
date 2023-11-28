from PIL import Image
import numpy as np

def logarithmic_transform(image, gamma, c):
    # Chuyển đổi ảnh thành mảng numpy
    image_array = np.array(image)

    # Áp dụng biến đổi logarithmic trên từng pixel
    transformed_array = c * np.log(1 + image_array.astype(np.float32))

    # Chuyển đổi lại thành ảnh PIL
    transformed_image = Image.fromarray(transformed_array.astype(np.uint8))

    return transformed_image

# Đường dẫn đến ảnh grayscale
image_path = "path/to/your/image.png"

# Đọc ảnh grayscale
grayscale_image = Image.open(image_path).convert("L")

# Chọn hệ số giai đoạn (gamma) và hệ số tỷ lệ (scaling factor)
gamma = 1.0
c = 255 / np.log(1 + grayscale_image.getextrema()[1])

# Áp dụng thuật toán Logarithmic Transform
transformed_result = logarithmic_transform(grayscale_image, gamma, c)

# Lưu ảnh kết quả
output_path = "path/to/save/transformed_image.png"
transformed_result.save(output_path)

# Hiển thị ảnh kết quả
transformed_result.show()