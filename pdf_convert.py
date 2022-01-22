from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import io

def pdf_edit(in_pdf_file,out_pdf_file,img_file): 
 

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    can.drawString(50, 730, "Jhon institute")
    can.drawString(90, 50, "It’s easy to play any musical instrument:all you have to do is touch ")
    can.drawString(90, 30, "the right key at the right time and the instrument will play itself.")
    x_start = 430
    y_start = 325
    can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()
 
    #move to the beginning of the StringIO buffer
    packet.seek(0)
 
    new_pdf = PdfFileReader(packet)
 
    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()
 
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)
 
    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()
 
 
