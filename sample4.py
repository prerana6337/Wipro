import os
file="shift.py"
if os.path.exists(file):
    size=os.path.getsize(file)
    print(f"File {file} exists and its size is {size} bytes.")
else:
    print(f"File {file} does not exist.")