|convert_images| image_thumbs |
|--|--|
|1. Install Pillow Library| 1. Install Pillow Library|
|	$ pip install pillow| 		$ pip install pillow|
|2. Run script |2. Run script |
|		$ python convert_images.py |		$ python image_thumbs.py|
|3. Enter the filepath to where the images are located |3. Enter filepath of images to be converted |
|4. Enter the original file type of the image (i.e. tiff, jpeg, jpg) |4. Image thumbnails will be placed in a folder named `image_thumbs`, located in the same directory as the python script. |
|5. Enter the desired file type of the image (i.e. tiff, jpeg, jpg) |5. Any files that might be corrupted and where not converted into a thumbnail will be written to a file named corrupted.txt. |
|6. Files will be located in a folder named converted_[filetype], in the same filepath entered in step 3.| |
# convert_images

This script converts images from one image type to another. 

1. Install Pillow Library

		$ pip install pillow

2. Run script 

		$ python convert_images.py

3. Enter the filepath to where the images are located

4. Enter the original file type of the image (i.e. tiff, jpeg, jpg)

5. Enter the desired file type of the image (i.e. tiff, jpeg, jpg)

6. Files will be located in a folder named converted_[filetype], in the same filepath 
entered in step 3.

# image_thumbs

1. Install Pillow Library

		$ pip install pillow

2. run script
	
		$ python image_thumbs.py

3. Enter filepath of images to be converted

4. Image thumbnails will be placed in a folder named `image_thumbs`, located in the same 
directory as the python script.

5. Any files that might be corrupted and where not converted into a thumbnail will be 
written to a file named corrupted.txt.
	
