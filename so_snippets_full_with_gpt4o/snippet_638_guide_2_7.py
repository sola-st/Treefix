import os # pragma: no cover

filename = 'example.txt' # pragma: no cover
atime = 1633029600 # pragma: no cover
mtime = 1633029600 # pragma: no cover
if os.path.exists(filename): os.remove(filename) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1158076/implement-touch-using-python
from l3.Runtime import _l_
try:
    import os
    _l_(13572)

except ImportError:
    pass
def func(filename):
    _l_(13577)

    if os.path.exists(filename):
        _l_(13576)

        os.utime(filename)
        _l_(13573)
    else:
        with open(filename,'a') as f:
            _l_(13575)

            pass
            _l_(13574)

os.utime(filename,(atime,mtime))
_l_(13578)

