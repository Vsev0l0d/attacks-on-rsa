def to_text(number: int):
    return number.to_bytes(4, byteorder='big').decode('cp1251')
