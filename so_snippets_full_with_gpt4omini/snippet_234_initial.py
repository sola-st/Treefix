# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(2579)

except ImportError:
    pass
os.path.abspath("mydir/myfile.txt")
_l_(2580)
'C:/example/cwd/mydir/myfile.txt'
_l_(2581)
try:
    import os
    _l_(2583)

except ImportError:
    pass
os.path.abspath("C:/example/cwd/mydir/myfile.txt")
_l_(2584)
'C:/example/cwd/mydir/myfile.txt'
_l_(2585)

