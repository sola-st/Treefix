# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(14796)

except ImportError:
    pass
os.path.abspath("mydir/myfile.txt")
_l_(14797)
'C:/example/cwd/mydir/myfile.txt'
_l_(14798)
try:
    import os
    _l_(14800)

except ImportError:
    pass
os.path.abspath("C:/example/cwd/mydir/myfile.txt")
_l_(14801)
'C:/example/cwd/mydir/myfile.txt'
_l_(14802)

