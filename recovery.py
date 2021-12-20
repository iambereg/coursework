import sys
from sys import argv
import struct
from struct import *

# input = 'test_numbers.bereg'
# bits = 15
input, bits = argv[1:]
table_size = pow(2, int(bits))
file = open(input, "rb")
compressed = []
next_code = 256
decompressed = ""
line = ""

while True:
    read_symbols = file.read(2)
    if len(read_symbols) != 2:
        break
    (data,) = unpack('>H', read_symbols)
    compressed.append(data)

dict_size = 256
dic = dict([(x, chr(x)) for x in range(dict_size)])

for code in compressed:
    if not (code in dic):
        dic[code] = line + (line[0])
    decompressed += dic[code]
    if not (len(line) == 0):
        dic[next_code] = line + (dic[code][0])
        next_code += 1
    line = dic[code]

out_name_file = input.split(".")[0]
output = open(out_name_file + "_gg.txt", "w")
for data in decompressed:
    output.write(data)

output.close()
file.close()