# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
from l3.Runtime import _l_
try:
    import os
    _l_(12437)

except ImportError:
    pass

my_fullpath = r"D:\MY_FOLDER\TEST\20201108\20201108_073751.DNG"
_l_(12438)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(12439)

my_fullpath = r"/MY_FOLDER/TEST/20201108/20201108_073751.DNG"
_l_(12440)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(12441)

my_fullpath = r"/MY_FOLDER/TEST/20201108/"
_l_(12442)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(12443)

my_fullpath = r"/MY_FOLDER/TEST/20201108"
_l_(12444)
os.path.basename(my_fullpath.replace('\\',os.sep))
_l_(12445)

