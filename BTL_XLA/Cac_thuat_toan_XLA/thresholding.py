from PIL import Image

def threshold_image(image, threshold):
    # Tạo một bản sao của ảnh đầu vào
    thresholded = image.copy()

    # Lấy kích thước của ảnh
    width, height = image.size

    # Lặp qua từng pixel trong ảnh
    for x in range(width):
        for y in range(height):
            # Lấy giá trị pixel tại vị trí (x, y)
            pixel = image.getpixel((x, y))

            # So sánh giá trị pixel với giá trị ngưỡng
            if pixel < threshold:
                # Pixel thuộc lớp dưới ngưỡng (background)
                thresholded.putpixel((x, y), 0)
            else:
                # Pixel thuộc lớp trên ngưỡng (foreground)
                thresholded.putpixel((x, y), 255)

    return thresholded

# Đường dẫn đến ảnh grayscale
image_path = "path/to/your/image.png"

# Đọc ảnh grayscale
grayscale_image = Image.open(image_path).convert("L")

# Chọn giá trị ngưỡng (threshold value)
threshold_value = 128

# Áp dụng thuật toán Thresholding
thresholded_result = threshold_image(grayscale_image, threshold_value)

# Lưu ảnh kết quả
output_path = "path/to/save/thresholded_image.png"
thresholded_result.save(output_path)

# Hiển thị ảnh kết quả
thresholded_result.show()