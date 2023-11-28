from PIL import Image

def negative_image(image):
    # Tạo một bản sao của ảnh đầu vào
    negative = image.copy()

    # Lấy kích thước của ảnh
    width, height = image.size

    # Lặp qua từng pixel trong ảnh
    for x in range(width):
        for y in range(height):
            # Lấy giá trị pixel tại vị trí (x, y)
            pixel = image.getpixel((x, y))

            # Đảo ngược giá trị của pixel
            inverted_pixel = 255 - pixel

            # Gán giá trị mới cho pixel trong ảnh negative
            negative.putpixel((x, y), inverted_pixel)

    return negative

# Đường dẫn đến ảnh grayscale
image_path = "path/to/your/image.png"

# Đọc ảnh grayscale
grayscale_image = Image.open(image_path).convert("L")

# Áp dụng thuật toán Negative Image
negative_result = negative_image(grayscale_image)

# Lưu ảnh kết quả
output_path = "path/to/save/negative_image.png"
negative_result.save(output_path)

# Hiển thị ảnh kết quả
negative_result.show()