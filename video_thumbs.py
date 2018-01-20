#This script requires that the python library 'opencv' is installed
#This can be done with the following command: pip install opencv-python
#The program takes a folder of images and grabs screen captures
#The spacer variable spaces how often screens are saved. 
#The spacer%100 == 0 tells the program that if spacer/100 has no remainder to save the image. This means that every 100 frames get saved. 
#
#This script assumes there is a file folder holding videos of some kind. If these videos are of different types, this script will have to run for each type.
import os
import cv2

filepath = input('Enter File Path: ') 
input_type = input('Enter Video Type: ')
count = 0
for file in os.listdir(filepath):  
	if file.endswith(".%s" % input_type): #if file is input_type video type
		path = os.path.join(filepath, file)
		vidcap = cv2.VideoCapture(path) #video capture of image
		savedirpath = os.path.join(filepath, "video_thumbs") #created a folder named video_thumbs
		if not os.path.exists(savedirpath): #creates folder if doesn't exist
			os.makedirs(savedirpath)
		count = 1
		spacer = 0
		while vidcap.isOpened(): #while videocapture is running
			success, image = vidcap.read() #read video
			if success and count < 6: #if success (boolean) is true and image thumbs are fewer than 5
				filename, ext = os.path.splitext(file)
				if spacer%100 == 0: #every 100 frames save image
					filename = filename + "_thumb_" + str(count) 
					cv2.imwrite(os.path.join(savedirpath, '%s.png') % filename, image)#writes file to savdirpath, with filename and write image
					count += 1
				spacer += 1
			else:
				break
		print("Success for file: %s" % file)
		cv2.destroyAllWindows() 
		vidcap.release()