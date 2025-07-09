import os
folder="prerana"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder '{folder}' created.")
else:
    print(f"Folder '{folder}' already exists.")

