import re

def process_line(line):
        
    line = re.sub(' ', '20', line)
    line = re.sub('a', '61', line)
    line = re.sub('b', '62', line)
    line = re.sub('c', '63', line)
    line = re.sub('d', '64', line)
    line = re.sub('e', '65', line)
    line = re.sub('f', '66', line)
    line = re.sub('g', '67', line)
    line = re.sub('h', '68', line)
    line = re.sub('i', '69', line)
    line = re.sub('j', '6a', line)
    line = re.sub('k', '6b', line)
    line = re.sub('l', '6c', line)
    line = re.sub('m', '6d', line)
    line = re.sub('n', '6e', line)
    line = re.sub('o', '6f', line)
    line = re.sub('p', '70', line)
    line = re.sub('q', '71', line)
    line = re.sub('r', '72', line)
    line = re.sub('s', '7+', line)
    line = re.sub('t', '74', line)
    line = re.sub('u', '75', line)
    line = re.sub('v', '76', line)
    line = re.sub('w', '77', line)
    line = re.sub('x', '78', line)
    line = re.sub('y', '79', line)
    line = re.sub('z', '7a', line)
    line = re.sub(':', '3a', line)

    print(line)

line1=raw_input()

process_line(line1)
