# Extracted from https://stackoverflow.com/questions/123198/how-to-copy-files
import shutil
shutil.copy2('/path/to/original/file', '/path/to/copy/file')

import os
with open('/path/to/original/file', 'rb') as f_src, open('/path/to/copy/file', 'wb') as f_dst:
    f_dst.write(f_src.read())

import subprocess
subprocess.run(['cp', '/path/to/original/file', '/path/to/copy/file'])

import fileinput
with fileinput.FileInput('/path/to/original/file', inplace=False, backup='.bak') as file, open('/path/to/copy/file', 'w') as f:
    for line in file:
        f.write(line)

import os
os.system("cp /path/to/original/file /path/to/copy/file")

with open("/path/to/original/file") as src, open("/path/to/copy/file", "w") as dst:
    dst.write(src.read())

import io

with io.FileIO("/path/to/original/file", "r") as src, io.FileIO("/path/to/copy/file", "w") as dst:
    dst.write(src.readall())

import mmap

with open("/path/to/original/file", "rb") as src, open("/path/to/copy/file", "wb") as dst:
    mmapped_src = mmap.mmap(src.fileno(), 0, access=mmap.ACCESS_READ)
    dst.write(mmapped_src[:])


1. Execution time shutil: 0.86 seconds
2. Execution time os: 0.92 seconds
3. Execution time subprocess: 6.65 seconds
4. Execution time fileinput: 7.03 seconds
5. Execution time os.system`: 12.79 seconds
6. Execution time file.write: 1.13 seconds
7. Execution time io.FileIO: 0.89 seconds
8. Execution time mmap: 21.86 seconds

1. Execution time shutil: 0.35 seconds
2. Execution time os: 0.17 seconds
3. Execution time subprocess: 5.55 seconds
4. Execution time fileinput: 0.26 seconds
5. Execution time os.system`: 10.75 seconds
6. Execution time file.write: 0.17 seconds
7. Execution time io.FileIO: 0.15 seconds
8. Execution time mmap: 20.53 seconds

