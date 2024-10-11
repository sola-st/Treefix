import os # pragma: no cover
import string # pragma: no cover

os = type('Mock', (object,), {'listdir': lambda x: ['/Users/tedfuller/Desktop/prank/file1.txt', '/Users/tedfuller/Desktop/prank/file2.txt'], 'chdir': lambda x: None, 'getcwd': lambda: '/Users/tedfuller/Desktop/prank', 'rename': lambda src, dst: None}) # pragma: no cover
string = type('Mock', (object,), {'digits': '0123456789'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2759067/rename-multiple-files-in-a-directory-in-python
#List all files in the directory
from l3.Runtime import _l_
file_list = os.listdir("/Users/tedfuller/Desktop/prank/")
_l_(13595)
print(file_list)
_l_(13596)

#Change current working directory and print out it's location
working_location = os.chdir("/Users/tedfuller/Desktop/prank/")
_l_(13597)
working_location = os.getcwd()
_l_(13598)
print(working_location)
_l_(13599)

#Rename all the files in that directory
for file_name in file_list:
    _l_(13601)

    os.rename(file_name, file_name.translate(str.maketrans("","",string.digits)))
    _l_(13600)

