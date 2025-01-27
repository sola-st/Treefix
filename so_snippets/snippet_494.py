# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(2550)

except ImportError:
    pass
try:
    import inspect
    _l_(2552)

except ImportError:
    pass
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
_l_(2553)
parentdir = os.path.dirname(currentdir)
_l_(2554)
os.sys.path.insert(1, parentdir)
_l_(2555)
# print("currentdir = ", currentdir)
# print("parentdir=", parentdir)

