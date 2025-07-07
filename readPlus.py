with open('file1.txt','r+') as file:
    content = file.read()
    print(content)  # Read the entire file
    file.seek(10)  # Move the cursor back to the beginning of the file
    print(file.read(10))  # Read the next 10 bytes