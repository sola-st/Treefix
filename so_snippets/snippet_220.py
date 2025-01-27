# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
from l3.Runtime import _l_
try:
    import os
    _l_(412)

except ImportError:
    pass
try:
    import inspect
    _l_(414)

except ImportError:
    pass
inspect.getfile(os)
_l_(415)
'/usr/lib64/python2.7/os.pyc'
_l_(416)
inspect.getfile(inspect)
_l_(417)
'/usr/lib64/python2.7/inspect.pyc'
_l_(418)
os.path.dirname(inspect.getfile(inspect))
_l_(419)
'/usr/lib64/python2.7'
_l_(420)

