'''with open("file1.txt", 'r') as file:
    lines=file.readlines()
print("List of lines:", lines)'''
'''with open("file1.txt", 'r') as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())  # Using strip() to remove newline characters'''
'''with open("file1.txt", 'r') as file:
    separate_lines=[line.strip() for line in file.readlines()]
    print(separate_lines)'''
'''
file=open("file1.txt", 'r')
print(file.close())
file.close()
print(file.closed)  # Check if the file is closed'''

'''program to create a text file access the txt file data
 and use the data to split the lines into series of 
 words and use space to perform the split operation
 sample.txt
 hello students
 how are you today
 output:
 ['Hello', 'students', 'how', 'are', 'you', 'today']'''
    