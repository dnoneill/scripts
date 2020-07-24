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


# tesseract

This script will OCR a PDF. Run the script and enter the filepath of the PDF. It renders a docx copy of the OCRed text and a PDF copy.

1. python tesseract.py
2. Enter filepath of PDF
3. Hit enter

