import os # pragma: no cover
import sys # pragma: no cover

sys.path.append(os.path.join(os.path.expanduser('~'), 'Desktop')) # pragma: no cover
type('Mock', (object,), {'test_function': lambda: 'mocked response'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(13699)

except ImportError:
    pass

