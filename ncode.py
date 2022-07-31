open('C:\-\НРИ\Книжки\Охота_на_охотников.pdf', 'w', encoding='cp500').write('Hello\n')


encoding = [
'utf-8',
'cp500',
'utf-16',
'GBK',
'windows-1251',
'ASCII',
'US-ASCII',
'Big5'
]

correct_encoding = ''

for enc in encoding:
    try:
        open('C:\-\НРИ\Книжки\Фея Темные Века.pdf', encoding=enc).read()
    except (UnicodeDecodeError, LookupError):
        pass
    else:
        correct_encoding = enc
        print('Done!')
        break


print(correct_encoding)