from PIL import Image
import os


# dir_path = 'D:\\Projects\Python\\test\\emergency_sign\\test'
dir_path = './images'

# Get all image files in the directory
files = os.listdir(dir_path)
image_files = [file for file in files if file.endswith(("png", "jpg", "jpeg"))]

# Mirror each image and save it to the output directory
for file in image_files:
    with Image.open(os.path.join(dir_path, file)) as img:
        mirrored_img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
        mirrored_img.save(os.path.join(dir_path, "mirrored_" + file))
