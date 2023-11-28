def lzw_encode(data):
    dictionary = {}
    next_code = 256
    encoded_data = []
    current_sequence = data[0]
    for symbol in data[1:]:
        new_sequence = current_sequence + symbol
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            encoded_data.append(dictionary[current_sequence])
            dictionary[new_sequence] = next_code
            next_code += 1
            current_sequence = symbol
    encoded_data.append(dictionary[current_sequence])
    return encoded_data


def lzw_decode(encoded_data):
    dictionary = {code: chr(code) for code in range(256)}
    next_code = 256
    decoded_data = ""
    previous_code = encoded_data[0]
    decoded_data += dictionary[previous_code]
    for code in encoded_data[1:]:
        if code in dictionary:
            sequence = dictionary[code]
        else:
            sequence = dictionary[previous_code] + dictionary[previous_code][0]
        decoded_data += sequence
        dictionary[next_code] = dictionary[previous_code] + sequence[0]
        next_code += 1
        previous_code = code
    return decoded_data


# Chuỗi dữ liệu gốc
original_data = "ABABABA"

# Mã hóa chuỗi dữ liệu
encoded_data = lzw_encode(original_data)
print("Encoded data:", encoded_data)

# Giải mã chuỗi dữ liệu
decoded_data = lzw_decode(encoded_data)
print("Decoded data:", decoded_data)