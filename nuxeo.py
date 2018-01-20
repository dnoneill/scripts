#This script assumes that the file is a Tab Separated Value file (tsv)
#It assumes that the columns.txt is in the same filepath as the entered filepath and the file is named columns.txt
#It also requires that pandas library is installed: ****pip install pandas****
#It also assumes that columns with numbers are set and not changed
#Written by Niqui O'Neill
import csv
import os
import re
import pandas as pd
filepath = input('Enter File Path: ') 
columns_txt = os.path.join(filepath, "columns.txt")
columns_list = []
with open(columns_txt, 'r') as columns_file:  ##Adds all headers in columns.txt to list
	for column in columns_file:
		if column != '\n':
			columns_list.append(column.strip("\n").strip(" "))
for file in os.listdir(filepath): 
	if file.endswith(".tsv"):  ## line 12-13 check files in filepath and checks to make sure they are tsv
		with open(file) as tsv: #opens file
			tsvreader = csv.DictReader(tsv, delimiter="\t") #uses csv reader to read file
			headers = tsvreader.fieldnames #grabs first row
			tsv_headers = [] 
			creator = []
			description = []
			subject = []
			place = []
			subject_topic = []
			form = []
			for header in headers: #cycles through headers in tsv file
				if bool(re.search(r'\d', header)) == True: #checks to see if there is a number in the header
					if bool(re.search(r'\Creator', header)) == True: #checks to see if specific fields
						creator.append(header)
					if bool(re.search(r'\Description ', header)) == True:
						description.append(header)
					if bool(re.search(r'\Subject (Name)', header)) == True:
						subject.append(header)
					if bool(re.search(r'\Place', header)) == True:
						place.append(header)
					if bool(re.search(r'\Subject (Topic)', header)) == True:
						subject_topic.append(header)
					if bool(re.search(r'\Form/Genre', header)) == True:
						form.append(header)
				tsv_headers.append(re.sub('\d+', '%d', header)) #add headers to list, replaces any numbers with %d to match against list				
			print("Missing fields in %s" % file)
			missing = []
			for column in columns_list: #columns.txt list
				if column not in tsv_headers: #checks to see if header in columns.txt are in headers in the tsv file
					missing.append(column) #if header in columns.txt is not in tsv file, adds header to list
			if len(creator) % 5 != 0:  ##lines 44-97 check for special fields with numbers
				high_numb = int(len(creator)/5) + 1 #gets the highest number for these types of columns
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Creator', column)): #finds creator fields in the required fields list
							if column%i not in headers: #formats the column with the number, checks to see if in tsv file
								missing.append(column%i) # if not there add to missing list
					i -=1 #go to next number
			if len(description) % 2 != 0:
				high_numb = int(len(description)/2) + 1
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Description ', column)):
							if column%i not in headers:
								missing.append(column%i)
					i -=1
			if len(subject) % 5 != 0:
				high_numb = int(len(subject)/5) + 1
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Subject (Name)', column)):
							if column%i not in headers:
								missing.append(column%i)
					i -=1
			if len(place) % 4 != 0:
				high_numb = int(len(place)/4) + 1
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Place', column)):
							if column%i not in headers:
								missing.append(column%i)
					i -=1
			if len(subject_topic) % 4 != 0:
				high_numb = int(len(subject_topic)/4) + 1
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Subject (Topic)', column)):
							if column%i not in headers:
								missing.append(column%i)
					i -=1
			if len(form) % 4 != 0:
				high_numb = int(len(form)/4) + 1
				i = high_numb
				while i > 0:
					for column in columns_list:
						if bool(re.search(r'\Form/Genre', column)):
							if column%i not in headers:
								missing.append(column%i)
					i -=1	
			header_list = headers #sets a header list to headers in tsv file (line 16)
			for miss in missing: #cycles through missing headers
				header_list.append(miss) #appends to list of headers in tsv file
			if len(missing) > 0:
				df = pd.read_csv(file, sep='\t') #uses pandas to read tsv file
				with_missing = df.reindex(columns=header_list) #reindexes columns to add missing headers
				with_missing.to_csv(file, sep='\t', index=False) #writes to tsv file
				print("Missing %s fields: %s have been added\n"%(len(missing),missing))
			else:
				print("****All Fields Present!*****\n")
			