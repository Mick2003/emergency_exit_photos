from PIL import Image
import os

directory = './images'  # replace with the path to your directory


for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        # open the image and rotate it
        with Image.open(os.path.join(directory, filename)) as img:
            rotated_img = img.rotate(-90, expand=True)
            # save the rotated image with the same filename
            rotated_img.save(os.path.join(directory, filename))