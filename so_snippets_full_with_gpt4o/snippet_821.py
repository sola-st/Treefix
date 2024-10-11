# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/918154/relative-paths-in-python
from l3.Runtime import _l_
try:
    import ntpath
    _l_(12451)

except ImportError:
    pass
try:
    import os
    _l_(12453)

except ImportError:
    pass
dirname = ntpath.dirname(__file__)
_l_(12454)
filename = os.path.join(dirname, 'relative/path/to/file/you/want')
_l_(12455)

