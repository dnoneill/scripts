#!/usr/bin/env python
#This script takes an input filetype and counts all files of that type in the inputed filepath and all subfolders in that filepath
#It will then write the filepath, filetype and total count to a csv file. 
#The script will continue until 'q' is entered.
__author__      = "Niqui O'Neill"

import os
import csv
import datetime
quit = 'a'
while quit is not 'q':
	count = 0
	print('{0:*^80}'.format('**'))
	filepath = input('Enter File Path: ') 
	type = input('Enter File Type (i.e. tif, jpg, xml): ')
	for root, dirs, files in os.walk(filepath):
		for file in files:
			if file.endswith(".%s" % type):
				count += 1
	print('\nCount: %s' % count)
	filename = 'filecount_{}.csv'.format(datetime.datetime.now().date())
	with open(filename, 'a', newline='') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow([filepath, type, count])
	quit = input('Enter q to quit, enter any other key to continue: ')