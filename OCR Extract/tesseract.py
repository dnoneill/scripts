try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from wand.image import Image as wi
import os, sys
import fitz
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter
import docx

output = PdfFileWriter()
try:
    f = raw_input("Enter the path of your PDF: ")
except:
    f = input("Enter the path of your PDF: ")

fullstring = ""
with(wi(filename=f, resolution=120)) as source:
    for i, image in enumerate(source.sequence):
        fp = tempfile.NamedTemporaryFile(suffix='.jpg')
        wi(image).save(filename=fp.name)
        pdf = pytesseract.image_to_pdf_or_hocr(Image.open(fp.name), extension='pdf')
        fullstring += pytesseract.image_to_string(Image.open(fp.name)) + "\n"
        tmppdf = tempfile.NamedTemporaryFile(suffix='.pdf')
        with open(tmppdf.name, 'w+b') as pdffile:
            pdffile.write(pdf) # pdf type is bytes by default
        pdf = PdfFileReader(tmppdf.name, "rb")
        output.addPage(pdf.getPage(0))
ocrfilename = f.replace(".pdf", "-ocr.pdf")
with open(ocrfilename, 'wb') as ocrfile:
    output.write(ocrfile)


ocrfilenamedoc = f.replace(".pdf", "-ocr.docx")
doc = docx.Document()
for para in fullstring.split("\n"):
    doc.add_paragraph(para)
doc.save(ocrfilenamedoc)
