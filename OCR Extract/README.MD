# altoocr_issue and altoocr_article

Both these scripts will convert ocr xml files into plain text files.
Issue just grabs all the data in the xml file. Article splits the text files into articles 
based on the data in the MET.xml file.
They both assume a file structure of:
ISSUE/filename
   ALTO
       filename--0001.xml
   OCRmaster
       filename--0001.jp2        
   Viewing
       filename--0001.jp2   
   filename-METS.xml


1. Run script

