import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Hàm xử lý ảnh với thuật toán Negative Transform
def negative_transform(image):
    negative_image = 255 - image
    return negative_image

# Hàm xử lý ảnh với thuật toán Thresholding
def thresholding(image, threshold):
    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresholded_image

# Hàm xử lý ảnh với thuật toán Logarithmic Transform
def logarithmic_transform(image, c):
    logarithmic_image = c * np.log1p(image)
    logarithmic_image = np.array(logarithmic_image, dtype=np.uint8)
    return logarithmic_image

# Hàm xử lý ảnh với thuật toán Histogram Equalization
def histogram_equalization(image):
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

# Hàm xử lý ảnh với Median Filter
def median_filter(image, kernel_size):
    median_filtered_image = cv2.medianBlur(image, kernel_size)
    return median_filtered_image

# Hàm xử lý ảnh với toán tử Roberts
def roberts_operator(image):
    roberts_image = cv2.roberts(image)
    return roberts_image

# Hàm xử lý ảnh với toán tử Sobel
def sobel_operator(image):
    sobel_image = cv2.Sobel(image, cv2.CV_8U, 1, 1, ksize=3)
    return sobel_image

# Hàm xử lý ảnh với toán tử Laplacian
def laplacian_operator(image):
    laplacian_image = cv2.Laplacian(image, cv2.CV_8U)
    return laplacian_image

# Hàm xử lý ảnh với phương pháp Canny
def canny_edge_detection(image, threshold1, threshold2):
    canny_image = cv2.Canny(image, threshold1, threshold2)
    return canny_image

# Hàm xử lý ảnh với phương pháp Otsu
def otsu_thresholding(image):
    _, otsu_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsu_image

# Hàm xử lý chọn ảnh từ file
def select_image():
    path = filedialog.askopenfilename()
    if path:
        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        original_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        original_image = Image.fromarray(original_image)
        original_image.thumbnail((400, 400))
        img_label.configure(image=ImageTk.PhotoImage(original_image))
        img_label.image = original_image
        process_button.configure(state=tk.NORMAL)
        global processed_image
        processed_image = image.copy()

# Hàm xử lý ảnh khi nhấn nút xử lý
def process_image():
    algorithm = algorithm_var.get()
    
    if algorithm == "Negative Transform":
        processed_image = negative_transform(processed_image)
    elif algorithm == "Thresholding":
        threshold = threshold_var.get()
        processed_image = thresholding(processed_image, threshold)
    elif algorithm == "Logarithmic Transform":
        c = c_var.get()
        processed_image = logarithmic_transform(processed_image, c)
    elif algorithm == "Histogram Equalization":
        processed_image = histogram_equalization(processed_image)
    elif algorithm == "Median Filter":
        kernel_size = kernel_size_var.get()
        processed_image = median_filter(processed_image, kernel_size)
    elif algorithm == "Roberts Operator":
        processed_image = roberts_operator(processed_image)
    elif algorithm == "Sobel Operator":
        processed_image = sobel_operator(processed_image)
    elif algorithm == "Laplacian Operator":
        processed_image = laplacian_operator(processed_image)
    elif algorithm == "Canny Edge Detection":
        threshold1 = threshold1_var.get()
        threshold2 = threshold2_var.get()
        processed_image = canny_edge_detection(processed_image, threshold1, threshold2)
    elif algorithm == "Otsu Thresholding":
        processed_image = otsu_thresholding(processed_image)
    
    processed_image = Image.fromarray(processed_image)
    processed_image.thumbnail((400, 400))
    processed_label.configure(image=ImageTk.PhotoImage(processed_image))
    processed_label.image = processed_image

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Image Processing")
window.geometry("800x600")

# Tạo các thành phần giao diện
select_button = tk.Button(window, text="Select Image", command=select_image)
select_button.pack(pady=10)

algorithm_var = tk.StringVar()
algorithm_var.set("Negative Transform")

algorithm_label = tk.Label(window, text="Select Algorithm:")
algorithm_label.pack()

algorithm_menu = tk.OptionMenu(window, algorithm_var, "Negative Transform", "Thresholding", "Logarithmic Transform",
                               "Histogram Equalization", "Median Filter", "Roberts Operator", "Sobel Operator",
                               "Laplacian Operator", "Canny Edge Detection", "Otsu Thresholding")
algorithm_menu.pack(pady=10)

threshold_frame = tk.Frame(window)

threshold_label = tk.Label(threshold_frame, text="Threshold:")
threshold_label.pack(side=tk.LEFT)

threshold_var = tk.IntVar()
threshold_slider = tk.Scale(threshold_frame, from_=0, to=255, variable=threshold_var, orient=tk.HORIZONTAL)
threshold_slider.pack(side=tk.LEFT)

threshold_frame.pack()

c_frame = tk.Frame(window)

c_label = tk.Label(c_frame, text="c:")
c_label.pack(side=tk.LEFT)

c_var = tk.DoubleVar()
c_slider = tk.Scale(c_frame, from_=0.1, to=10.0, resolution=0.1, variable=c_var, orient=tk.HORIZONTAL)
c_slider.pack(side=tk.LEFT)

c_frame.pack()

kernel_size_frame = tk.Frame(window)

kernel_size_label = tk.Label(kernel_size_frame, text="Kernel Size:")
kernel_size_label.pack(side=tk.LEFT)

kernel_size_var = tk.IntVar()
kernel_size_slider = tk.Scale(kernel_size_frame, from_=3, to=15, variable=kernel_size_var, orient=tk.HORIZONTAL)
kernel_size_slider.pack(side=tk.LEFT)

kernel_size_frame.pack()

threshold1_frame = tk.Frame(window)

threshold1_label = tk.Label(threshold1_frame, text="Threshold 1:")
threshold1_label.pack(side=tk.LEFT)

threshold1_var = tk.IntVar()
threshold1_slider = tk.Scale(threshold1_frame, from_=0, to=255, variable=threshold1_var, orient=tk.HORIZONTAL)
threshold1_slider.pack(side=tk.LEFT)

threshold1_frame.pack()

threshold2_frame = tk.Frame(window)

threshold2_label = tk.Label(threshold2_frame, text="Threshold 2:")
threshold2_label.pack(side=tk.LEFT)

threshold2_var = tk.IntVar()
threshold2_slider = tk.Scale(threshold2_frame, from_=0, to=255, variable=threshold2_var, orient=tk.HORIZONTAL)
threshold2_slider.pack(side=tk.LEFT)

threshold2_frame.pack()

process_button = tk.Button(window, text="Process Image", command=process_image, state=tk.DISABLED)
process_button.pack(pady=10)

img_label = tk.Label(window)
img_label.pack()

processed_label = tk.Label(window)
processed_label.pack()

# Chạy chương trình
window.mainloop()