import bitarray

def f2b(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_string = bitarray.bitarray()
            binary_string.fromfile(file)
        return binary_string.to01()
    except IOError:
        print(f"Unable to open file: {file_path}")
        return ''