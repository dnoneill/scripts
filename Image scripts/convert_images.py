#!/usr/bin/env python
#This script requires the user to input the filepath of where the images are located
#converts the images of the inputed original type (tif, jpg, png)
#into the output type. The input and output type need to be the extension (tif vs tiff)
#It then saves the converted images into a folder named converted_[output_type] located in the image file directory
#requires PILLOW library; pip install pillow
__author__      = "Niqui O'Neill"

from PIL import Image
import os
import sys
import time
import datetime

filepath = input('Enter File Path: ') 
input_type = input('Enter Original Type (Extension): ')
output_type = input('Enter Desired Type (Extension): ')
count = 0
for file in os.listdir(filepath): 
    if file.endswith(".%s" % input_type): #if file ends with input_type
        path = os.path.join(filepath, file) #path = filepath + file
        im = Image.open(path) #opens file
        filename = os.path.splitext(file)[0] #filename without extension
        output_file = "%s.%s" % (filename, output_type) #filename with new filetype
        savedir = "converted_%s" % output_type #directory where files are saved, named converted_[output_type]
        savedirpath = os.path.join(filepath, savedir)
        if not os.path.exists(savedirpath):#makes directory if it does not exist
            os.makedirs(savedirpath)
        imagepath = os.path.join(savedirpath, output_file)  #image filepath
        if 'jpeg' in output_type or 'jpg' in output_type:
            im = im.convert('RGB')
        im.save(imagepath) #saves image
        count += 1 #counts the number of files
        sys.stdout.write("\rFiles done: %s  Time Elapsed: %s" % (count, datetime.timedelta(seconds=int(time.clock())))) #writes number of files done, how much time has elapsed
        sys.stdout.flush()
        time.sleep(0.25)
sys.stdout.write("\n")#newline after script is done
			
