path_file = input('Write file path\n')
file = open(path_file, 'a', encoding='utf-8')
while True:
    text = "".join(iter(input, ""))
    if text == 'stop':
        break
    else:
        text = text.replace('-', '')
        file.write(text)
        print('done')
file.close()