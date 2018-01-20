#based upon python alto_ocr_text.py located here: https://github.com/cneud/alto-ocr-text


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
                        if article.attrib.get("TYPE") == 'ARTICLE':
                            id = article.attrib.get("DMDID")
                            title = article.attrib.get("LABEL")
                            if title != None:
                                articledict[id] = title
                if file.endswith(".xml"):
                    with open(os.path.join(filepath2, 'ALTO', file)) as data:
                        #print(file)
                        all_text = ''
                        tree = ET.parse(data)
                        styledict = {}
                        for style in tree.iterfind('.//TextStyle'):
                            id = style.attrib.get('ID')
                            fontstyle = style.attrib.get('FONTSTYLE')
                            styledict[id] = fontstyle
                        for lines in tree.iterfind('.//TextBlock'):
                            for line in lines.iterfind('.//TextLine'):
                                #all_text += "\n"
                                #sys.stdout.write('\n')
                                for lin in line.findall('String'):
       
                                    text = lin.attrib.get('CONTENT') + ' '
                                    
                                    all_text += text
                                    #sys.stdout.write(text)
                
                indexes = []
                found = {}
                if len(articledict) > 0:
                    for key, value in sorted(articledict.items()):
                        text = {}
                        index = all_text.find(value)
                        front = key.split("ARTICLE")[0]
                        numb = key.split("ARTICLE")[1]
                        if len(numb) == 1:
                            numb = "0%s"%numb
                        article = front + "ARTICLE" + numb
                        found[article] = {'title':value, 'index':index}
                        if index != -1 and index != 0:
                            indexes.append(index - 1)
                x = 0
                if 0 not in indexes and len(indexes) > 0:
                    indexes.append(0)
                filename = file.replace(".xml", "")
                indexes = sorted(indexes)
                with open("W:/SBB_00008_articlefiles/%s_ARTICLE_TITLES.txt"%filename, 'w') as info:
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
                if len(indexes) > 0:
                    while x < len(indexes):
                        #print(indexes)
                        if len(str(x)) == 1:
                            number = "0%s"%str(x)
                        else:
                            number = str(x)
                        if x != len(indexes) - 1:  
                            with open("W:/SBB_00008_articlefiles/%s_ARTICLE%s.txt"%(filename, number), 'w') as article:
                                article.write(all_text[indexes[x]:indexes[x+1]])
                        else:
                            with open("W:/SBB_00008_articlefiles/%s_ARTICLE%s.txt"%(filename, number), 'w') as article:
                                article.write(all_text[indexes[x]:])
                        x += 1
                else:
                    with open("W:/SBB_00008_articlefiles/%s_ARTICLE.txt"%(filename), 'w') as f:
                        f.write(all_text)
                                            
                      