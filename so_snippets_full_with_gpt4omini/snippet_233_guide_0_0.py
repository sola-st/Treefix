import math # pragma: no cover
import sys # pragma: no cover

file_name = 'example_file.py' # pragma: no cover
sys.modules['example_file'] = type('Mock', (object,), {'__file__': file_name})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16869024/what-is-pycache
from l3.Runtime import _l_
try:
    import file_name
    _l_(1429)

except ImportError:
    pass

