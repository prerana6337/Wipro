import os
file="textfile.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"File {file} deleted.")
else:
    print(f"File {file} does not exist.")