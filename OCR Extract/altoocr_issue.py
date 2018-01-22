#!/usr/bin/env python
#This script assumes the following file structure for OCR files:
#ISSUE/filename
#   ALTO
#       filename--0001.xml
#   OCRmaster
#       filename--0001.jp2        
#   Viewing
#       filename--0001.jp2   
#   filename-METS.xml
#This script requires that the OCR text be in an xml file in the ALTO folder. All other folders do not need to exist.
__author__      = "Niqui O'Neill"

import codecs
import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

filepath = input("Enter OCR files filepath: ")
for file in os.listdir(filepath):
    filepath2 = os.path.join(filepath, file)
    for f in os.listdir(filepath2):
        if f == 'ALTO':
            for file in os.listdir(os.path.join(filepath2, f)):
                if file.endswith(".xml"):
                    with open(os.path.join(filepath2, 'ALTO', file)) as data:
                        print(file)
                        all_text = ''
                        tree = ET.parse(data)
                        for lines in tree.iterfind('.//TextLine'):
                            all_text += "\n"
                            for line in lines.findall('String'):
                                text = line.attrib.get('CONTENT') + ' '
                                all_text += text
            filename = file.replace(".xml", "")
            if not os.path.exists('issue_files'):
                os.makedirs('issue_files')
            with open("issue_files/%s.txt"%(filename), 'w') as f:
                f.write(all_text)