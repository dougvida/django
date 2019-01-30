import PyPDF2

pdf_file = open(r'testdata\joecommers.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

# get range from 0 to number_of_pages
for idx in range(5, number_of_pages):
    page = read_pdf.getPage(idx)
    page_content = page.extractText()
#    if page_content:
    print(page_content)

x = 0

