import sys
from sys import argv
from struct import *

# input = 'test_numbers.txt'
# bits = 15
input, bits = argv[1:]
table_size = pow(2, int(bits))
file = open(input)
data = file.read()

dict_size = 256
dic = {chr(i): i for i in range(dict_size)}
line = ""
compressed = []

for symbol in data:
    current_line = line + symbol
    if current_line in dic:
        line = current_line
    else:
        compressed.append(dic[line])
        if len(dic) <= table_size:
            dic[current_line] = dict_size
            dict_size += 1
        line = symbol

if line in dic:
    compressed.append(dic[line])

out_name_file = input.split(".")[0]
output = open(out_name_file + ".bereg", "wb")

for data in compressed:
    output.write(pack('>H', int(data)))

output.close()
file.close()