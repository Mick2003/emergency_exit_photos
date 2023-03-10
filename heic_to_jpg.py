from PIL import Image
import os

directory = './images'  # replace with the path to your directory

for filename in os.listdir(directory):
    if filename.endswith('.jpeg'):
        print('convering', filename)

        # open the image and convert to RGB if necessary
        with Image.open(os.path.join(directory, filename)) as img:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # save the image as a JPG with the same filename
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            img.save(os.path.join(directory, new_filename))

            # delete the original JPEG file
        os.remove(os.path.join(directory, filename))