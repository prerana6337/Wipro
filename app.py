with open("file1.txt", 'a+b') as file:
    file.write('Appeded data\n')
    file.seek(0)
    print(file.read())