data=b'This is a binary file.\n'
with open("binary_file.bin", "wb") as file:
    file.write(data)