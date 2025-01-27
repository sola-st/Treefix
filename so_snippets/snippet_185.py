# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
from l3.Runtime import _l_
try:
    import os
    _l_(470)

except ImportError:
    pass

my_fullpath = r"D:\MY_FOLDER\TEST\20201108\20201108_073751.DNG"
_l_(471)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(472)

my_fullpath = r"/MY_FOLDER/TEST/20201108/20201108_073751.DNG"
_l_(473)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(474)

my_fullpath = r"/MY_FOLDER/TEST/20201108/"
_l_(475)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(476)

my_fullpath = r"/MY_FOLDER/TEST/20201108"
_l_(477)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(478)

