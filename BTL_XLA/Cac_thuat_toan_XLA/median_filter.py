from PIL import Image
from statistics import median

def median_filter(image, window_size):
    # Chuyển đổi ảnh thành ảnh xám
    grayscale_image = image.convert("L")

    # Lấy kích thước ảnh
    width, height = grayscale_image.size

    # Kích thước của cửa sổ trượt
    half_window = window_size // 2

    # Tạo ảnh kết quả với cùng kích thước như ảnh gốc
    filtered_image = Image.new("L", (width, height))

    # Duyệt qua từng pixel trong ảnh
    for x in range(half_window, width - half_window):
        for y in range(half_window, height - half_window):
            # Lấy giá trị mức xám của các pixel trong cửa sổ
            pixels = []
            for i in range(-half_window, half_window + 1):
                for j in range(-half_window, half_window + 1):
                    pixel = grayscale_image.getpixel((x + i, y + j))
                    pixels.append(pixel)

            # Lấy giá trị trung vị của danh sách pixel
            median_value = median(pixels)

            # Gán giá trị trung vị cho pixel tại vị trí trung tâm của cửa sổ
            filtered_image.putpixel((x, y), int(median_value))

    return filtered_image

# Đường dẫn đến ảnh
image_path = "path/to/your/image.png"

# Đọc ảnh
image = Image.open(image_path)

# Kích thước của cửa sổ trượt
window_size = 3

# Áp dụng thuật toán Median Filter
filtered_result = median_filter(image, window_size)

# Lưu ảnh kết quả
output_path = "path/to/save/filtered_image.png"
filtered_result.save(output_path)

# Hiển thị ảnh kết quả
filtered_result.show()