import os # pragma: no cover
import string # pragma: no cover

os = type('MockOS', (object,), {'listdir': lambda x: ['file1.txt', 'file2.txt', 'file3.txt'], 'chdir': lambda x: None, 'getcwd': lambda: '/Users/tedfuller/Desktop/prank', 'rename': lambda x, y: None})() # pragma: no cover
string = type('MockString', (object,), {'digits': '0123456789'})() # pragma: no cover

import os # pragma: no cover
import string # pragma: no cover

os = type('MockOS', (object,), {'listdir': lambda path: ['file1.txt', 'file2.txt', 'file3.txt'], 'chdir': lambda path: None, 'getcwd': lambda: '/Users/tedfuller/Desktop/prank/', 'rename': lambda old, new: None})() # pragma: no cover
string = type('MockString', (object,), {'digits': '0123456789'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
#List all files in the directory
from l3.Runtime import _l_
file_list = os.listdir("/Users/tedfuller/Desktop/prank/")
_l_(2172)
print(file_list)
_l_(2173)

#Change current working directory and print out it's location
working_location = os.chdir("/Users/tedfuller/Desktop/prank/")
_l_(2174)
working_location = os.getcwd()
_l_(2175)
print(working_location)
_l_(2176)

#Rename all the files in that directory
for file_name in file_list:
    _l_(2178)

    os.rename(file_name, file_name.translate(str.maketrans("","",string.digits)))
    _l_(2177)

