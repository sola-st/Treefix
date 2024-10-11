# Extracted from https://stackoverflow.com/questions/1035340/reading-binary-file-and-looping-over-each-byte
import pathlib

for byte in pathlib.Path(path).read_bytes():
    print(byte)

with open(path, 'b') as file:
    for byte in file.read():
        print(byte)

with open(path, 'b') as file:
    callable = lambda: file.read(1024)
    sentinel = bytes() # or b''
    for chunk in iter(callable, sentinel): 
        for byte in chunk:
            print(byte)

from pathlib import Path
from functools import partial
from io import DEFAULT_BUFFER_SIZE

def file_byte_iterator(path):
    """given a path, return an iterator over the file
    that lazily loads the file
    """
    path = Path(path)
    with path.open('rb') as file:
        reader = partial(file.read1, DEFAULT_BUFFER_SIZE)
        file_iterator = iter(reader, bytes())
        for chunk in file_iterator:
            yield from chunk

import random
import pathlib
path = 'pseudorandom_bytes'
pathobj = pathlib.Path(path)

pathobj.write_bytes(
  bytes(random.randint(0, 255) for _ in range(2**20)))

l = list(file_byte_iterator(path))
len(l)
1048576

l[-100:]
[208, 5, 156, 186, 58, 107, 24, 12, 75, 15, 1, 252, 216, 183, 235, 6, 136, 50, 222, 218, 7, 65, 234, 129, 240, 195, 165, 215, 245, 201, 222, 95, 87, 71, 232, 235, 36, 224, 190, 185, 12, 40, 131, 54, 79, 93, 210, 6, 154, 184, 82, 222, 80, 141, 117, 110, 254, 82, 29, 166, 91, 42, 232, 72, 231, 235, 33, 180, 238, 29, 61, 250, 38, 86, 120, 38, 49, 141, 17, 190, 191, 107, 95, 223, 222, 162, 116, 153, 232, 85, 100, 97, 41, 61, 219, 233, 237, 55, 246, 181]
l[:100]
[28, 172, 79, 126, 36, 99, 103, 191, 146, 225, 24, 48, 113, 187, 48, 185, 31, 142, 216, 187, 27, 146, 215, 61, 111, 218, 171, 4, 160, 250, 110, 51, 128, 106, 3, 10, 116, 123, 128, 31, 73, 152, 58, 49, 184, 223, 17, 176, 166, 195, 6, 35, 206, 206, 39, 231, 89, 249, 21, 112, 168, 4, 88, 169, 215, 132, 255, 168, 129, 127, 60, 252, 244, 160, 80, 155, 246, 147, 234, 227, 157, 137, 101, 84, 115, 103, 77, 44, 84, 134, 140, 77, 224, 176, 242, 254, 171, 115, 193, 29]

    with open(path, 'rb') as file:
        for chunk in file: # text newline iteration - not for bytes
            yield from chunk

