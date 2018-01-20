#Written by Niqui O'Neill
#This script requires the pillow library to be downloaded: $pip install pillow
#This script requires the user to input the filepath of the folder where images are located
#If the file is in jp(e)g, bmp, png, gif, tif(f) format, a thumbnail for the image will be created in the same format
#The image dimensions will be 150 high or 150 wide and the other side will be sized automatically to scale
#The thumbnail files will be written to folder named 'image_thumbs' which will be in the same location as the image_thumbs.py script
#filename of thumbnails are [original filename]_thumbnail.[original filetype]
import os
from PIL import Image
filepath = input("Enter the filepath of image files: ")
imagetypes = ['.jpg', '.bmp', '.png', '.gif', '.tif', '.tiff', '.jpeg'] #filetypes
size = 150, 150 #image size
for file in os.listdir(filepath):
    infile, ext = os.path.splitext(file) #filename, extension
    if ext.lower() in imagetypes: #if the extension in lowercase is in the imagetypes list
        try:
            image = Image.open(os.path.join(filepath, file)) #open image
            image.thumbnail(size, Image.ANTIALIAS) #create thumbnail at size, Image.ANTIALIAS auto sizes
            if not os.path.exists('image_thumbs'): #image_thumbs file does not exists
                os.makedirs('image_thumbs') #make image_thumbs directory
            image.save("image_thumbs/%s_thumbnail%s"%(infile, ext)) #save image to image_thumbs in format: [original filename]_thumbnail.[original filetype]
        except:
            with open("image_thumbs/corrupted.txt", "a") as f: #if the thumbnail fails, open a text file named corrupted.txt
                f.write(file)  #writes the filename to corrupted.txt
                f.write("\n")
        