import os # pragma: no cover

os.makedirs('Desktop', exist_ok=True) # pragma: no cover
with open('Desktop/test.py', 'w') as f:# pragma: no cover
    f.write('x = 42') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(13699)

except ImportError:
    pass

