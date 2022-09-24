def print_number_to_text(number: int):
    print(number.to_bytes(4, byteorder='big').decode('cp1251'), end='')
