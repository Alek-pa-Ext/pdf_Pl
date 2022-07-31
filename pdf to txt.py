import pdfplumber
from pathlib import Path

file_path = input('Write file path\n')
pages = []
with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
    for page in pdf.pages:
        left = page.crop((0, 0, 0.5 * float(page.width), 0.95 * page.height))
        pages.append(left.extract_text())
        right = page.crop((0.51 * float(page.width), 0, page.width, 0.95 * page.height))
        pages.append(right.extract_text())

text = ''.join(pages)
text = text.replace('-\n', '')
text = text.replace('-\n', '')
text = text.replace('‑\n', '')
text = text.replace('\n', '')

file_name = Path(file_path).stem
with open(f'{file_path[:-len(file_name)-4]}\{file_name}.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(text)




