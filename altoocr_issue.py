#!/usr/bin/env python
# Usage: python alto_ocr_text.py <altofile>

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
                            #sys.stdout.write('\n')
                            for line in lines.findall('String'):
                                text = line.attrib.get('CONTENT') + ' '
                                all_text += text
                                #sys.stdout.write(text)
            filename = file.replace(".xml", "")
            with open("no_formatting/%s.txt"%(filename), 'w') as f:
                f.write(all_text)