"""
Simple script to reorder(based on name) files in a folder.

Format file: <int>.<ext>
Example:
    1.jpg
    2.jpg
    5.jpg

Output:
    1.jpg
    2.jpg
    3.jpg


Author: Mick Veenman
"""

import os

folder_paths = ["./images/test", './images/train']  # Replace with the path to your folder
# folder_path = "D:\\Projects\\Python\\test\\emergency_sign\\test"  # Replace with the path to your folder
# folder_path = "D:\\Projects\\Python\\test\emergency_sign\\train"  # Replace with the path to your folder


def reoder(folder_path):
    files = os.listdir(folder_path)

    for i, file_name in enumerate(files, 1):
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, f"{i}.jpg")
        os.rename(old_path, new_path)

def rename_all(folder_path):
    files = os.listdir(folder_path)
    exts = [".jpg", ".png", ".gif"]  # Replace with the file extensions you want to rename

    for i, file_name in enumerate(files):
        ext = os.path.splitext(file_name)[1].lower()
        if ext in exts:
            new_name = str(i + 1).zfill(5) + ext
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))


for folder_path in folder_paths:
    rename_all(folder_path)
    reoder(folder_path)