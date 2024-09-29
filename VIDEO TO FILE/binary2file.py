import bitarray

def b2f(binary_string, file_path):
    with open(file_path, 'wb') as file:
        for i in range(0, len(binary_string), 8):
            byte_str = binary_string[i:i+8]
            byte_value = int(byte_str, 2)
            file.write(bytes([byte_value]))
