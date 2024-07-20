#Step 1 create folder on desktop called Image_Editor
#Step 2 In folder Image_editor placed this py file
#Step 3 create new folder in Image_Editor called old_images and place photos you want to edit in there
#Step 4 create new folder on desktop call new_images
#Step 5 Run!

#Importing Pillow
from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./old_images" # folder for old images
pathOut = "./new_images" # folder for the edited images (on desktop)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # Sharpens image
    #edit = img.filter(ImageFilter.SHARPEN)

    #Makes black and white and details effect
    edit = img.filter(ImageFilter.DETAIL).convert('L')

    #Cool effect
    #edit = img.filter(ImageFilter.Find Edges)

    # contrast parameters
    factor = 1.2
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

#Saves in correct location and fixes
    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')