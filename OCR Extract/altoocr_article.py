#!/usr/bin/env python
#based upon python alto_ocr_text.py located here: https://github.com/cneud/alto-ocr-text
#This script assumes the following file structure for OCR files:
#ISSUE/filename
#   ALTO
#       filename--0001.xml
#   OCRmaster
#       filename--0001.jp2        
#   Viewing
#       filename--0001.jp2   
#   filename-METS.xml
#This script requires that the OCR text be in an xml file in the ALTO folder, and the METS file contains metadata including article names.
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
                metsfilename = file.split("-")[0]
                metsfilename = metsfilename + "-METS.xml"
                articledict = {}
                with open(os.path.join(filepath2, metsfilename)) as mets:
                    articletree = ET.parse(mets)
                    for article in articletree.iterfind(".//{http://www.loc.gov/METS/}div"):
                        if article.attrib.get("TYPE") == 'ARTICLE': #gets article names in metadata file
                            id = article.attrib.get("DMDID") #get id for article
                            title = article.attrib.get("LABEL") #get article title
                            if title != None:
                                articledict[id] = title
                if file.endswith(".xml"): #gets OCR text from xml in ALTO folder
                    with open(os.path.join(filepath2, 'ALTO', file)) as data:
                        all_text = ''
                        tree = ET.parse(data)
                        styledict = {}
                        for style in tree.iterfind('.//TextStyle'):
                            id = style.attrib.get('ID')
                            fontstyle = style.attrib.get('FONTSTYLE')
                            styledict[id] = fontstyle
                        for lines in tree.iterfind('.//TextBlock'):
                            for line in lines.iterfind('.//TextLine'):
                                for lin in line.findall('String'):
                                    text = lin.attrib.get('CONTENT') + ' '
                                    all_text += text
                
                indexes = []
                found = {}
                if len(articledict) > 0: #section cleans articles, gets indexes of article titles
                    for key, value in sorted(articledict.items()):
                        text = {}
                        index = all_text.find(value) #finds article title in OCR text
                        front = key.split("ARTICLE")[0] 
                        numb = key.split("ARTICLE")[1] #splits to allow article1 to be converted to article01
                        if len(numb) == 1:
                            numb = "0%s"%numb
                        article = front + "ARTICLE" + numb #puts article id back together
                        found[article] = {'title':value, 'index':index}
                        if index != -1 and index != 0:
                            indexes.append(index - 1)
                
                if 0 not in indexes and len(indexes) > 0:
                    indexes.append(0)
                filename = file.replace(".xml", "")
                indexes = sorted(indexes)
                new_files_dir = 'articlefiles'
                if not os.path.exists(new_files_dir):
                    os.makedirs(new_files_dir)
                with open("%s/%s_ARTICLE_TITLES.txt"%(new_files_dir, filename), 'w') as info:
                    for key, value in sorted(found.items()):
                        info.write(key)
                        info.write(": ")
                        info.write(value['title'])
                        info.write("\n")
                        if value['index'] == -1:
                            info.write("Not Found")
                        else:
                            info.write("Found")
                        info.write("\n")
                x = 0
                if len(indexes) > 0:
                    while x < len(indexes):
                        if len(str(x)) == 1:
                            number = "0%s"%str(x)
                        else:
                            number = str(x)
                        if x != len(indexes) - 1:  
                            with open("%s/%s_ARTICLE%s.txt"%(new_files_dir, filename, number), 'w') as article:
                                article.write(all_text[indexes[x]:indexes[x+1]])
                        else:
                            with open("%s/%s_ARTICLE%s.txt"%(new_files_dir, filename, number), 'w') as article:
                                article.write(all_text[indexes[x]:])
                        x += 1
                else:
                    with open("%s/%s_ARTICLE.txt"%(new_files_dir, filename), 'w') as f:
                        f.write(all_text)
                                            
                      