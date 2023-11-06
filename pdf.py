import PyPDF2
import sys
from constants import CONST_PDF_ROOT_DIRECTORY

# def combine_pdfs(pdf_list):
#     merger = PyPDF2.PdfFileMerger()

#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('./pdf_files/merged_pdf.pdf')

# inputs = sys.argv[1:]

# combine_pdfs(inputs)



def put_watermark(watermark_pdf_file, pdf_file):
    watermark_pdf = PyPDF2.PdfReader(open(f'{CONST_PDF_ROOT_DIRECTORY}{watermark_pdf_file}',"rb"))
    pdf_to_protect = PyPDF2.PdfReader(open(f'{CONST_PDF_ROOT_DIRECTORY}{pdf_file}',"rb"))
    output_pdf = PyPDF2.PdfWriter()

    for i in range(pdf_to_protect.getNumPages()):
        page = pdf_to_protect.getPage(i)
        page.mergePage(watermark_pdf.getPage(0))
        output_pdf.addPage(page)

        with open(f'{CONST_PDF_ROOT_DIRECTORY}watermarked.pdf',"wb") as watermarked_pdf:
            output_pdf.write(watermark_pdf)
            print(f'File watermarked: {watermark_pdf}')



input_pdf_file = sys.argv[1]

put_watermark(input_pdf_file)

# with open('./pdf_files/dummy.pdf',"rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfWriter
#     writer.addPage(page)
#     with open('./pdf_files/blah.pdf', "wb") as new_file:
#         writer.write(new_file)

