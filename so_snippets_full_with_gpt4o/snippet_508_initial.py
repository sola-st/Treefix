# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2589711/find-full-path-of-the-python-interpreter
from l3.Runtime import _l_
try:
    import sys
    _l_(15085)

except ImportError:
    pass

print(sys.executable)
_l_(15086)

