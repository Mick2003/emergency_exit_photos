import os

folder_path = "./images"  # Replace with the path to your folder
files = os.listdir(folder_path)

for i, file_name in enumerate(files, 1):
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, f"{i}.jpg")
    os.rename(old_path, new_path)