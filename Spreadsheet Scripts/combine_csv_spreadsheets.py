#!/usr/bin/env python
#This script takes multiple csv files and combines them into one csv file named combine_[input_filepath].csv
#Requires unicodecsv installed (pip install unicodecsv)
__author__      = "Niqui O'Neill"

import os
import unicodecsv as csv

data = []
filepath = input("Enter filepath: ")
for item in os.listdir(filepath):
    if item.endswith(".csv"):
        with open(os.path.join(filepath,item), 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

headers = []
for dict in data:
    for key in dict:
        if key not in headers:
            headers.append(key)
with open(os.path.join(filepath,"combine_%s.csv"%filepath), 'wb') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
