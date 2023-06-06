import re

def filter_from_text(text, search):
    result = simple_extraction(text, search)

    if result == '':
        result = lines_extraction(text, search)

    return result

def simple_extraction(text, search):
    search = search + ':'
    pattern = r'^.*{}.*$'.format(re.escape(search))
    lines = re.findall(pattern, text, re.MULTILINE)

    if len(lines) == 0:
        print('***' + search + ' not found!')
        return
    
    return lines[0].split(search)[1].lstrip()

def lines_extraction(text, search):
    search = search + ':'
    pattern = r'^.*{}.*\n.*$'.format(search)
    lines = re.findall(pattern, text, re.MULTILINE)
    
    if len(lines) == 0:
        print('***' + search + ' not found!')
        return
    
    return lines[0].split(search)[1].lstrip()

def remove_spaces(string):
    cleaned_string = string.replace(" ", "")
    return cleaned_string
