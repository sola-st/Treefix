import os # pragma: no cover

filename = 'uncreated_file.txt' # pragma: no cover
atime = 1234567890.0 # pragma: no cover
mtime = 1234567890.0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1158076/implement-touch-using-python
from l3.Runtime import _l_
try:
    import os
    _l_(3357)

except ImportError:
    pass
def func(filename):
    _l_(3362)

    if os.path.exists(filename):
        _l_(3361)

        os.utime(filename)
        _l_(3358)
    else:
        with open(filename,'a') as f:
            _l_(3360)

            pass
            _l_(3359)

os.utime(filename,(atime,mtime))
_l_(3363)

