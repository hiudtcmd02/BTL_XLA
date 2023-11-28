def run_length_encode(data):
    encoded_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_data += str(count) + data[i - 1]
            count = 1
    encoded_data += str(count) + data[-1]
    return encoded_data


def run_length_decode(encoded_data):
    decoded_data = ""
    i = 0
    while i < len(encoded_data):
        count = int(encoded_data[i])
        character = encoded_data[i + 1]
        decoded_data += character * count
        i += 2
    return decoded_data


# Chuỗi dữ liệu gốc
original_data = "AAABBBCCCDDDD"

# Mã hóa chuỗi dữ liệu
encoded_data = run_length_encode(original_data)
print("Encoded data:", encoded_data)

# Giải mã chuỗi dữ liệu
decoded_data = run_length_decode(encoded_data)
print("Decoded data:", decoded_data)