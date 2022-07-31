import pdfplumber

with pdfplumber.PDF(open(file='C:\-\НРИ\Книжки\Охота_на_охотников.pdf', mode='rb')) as pdf:
    print(pdf.pages[6].extract_text())