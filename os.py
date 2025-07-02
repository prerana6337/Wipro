import os
folder=input("Enter folder name to create:")
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder ''{folder}'' created sucessfully.")
else:
    print(f"Folder ''{folder}'' already exists.")