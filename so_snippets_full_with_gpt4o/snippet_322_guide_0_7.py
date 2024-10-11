import os # pragma: no cover
import sys # pragma: no cover

class MockModule:# pragma: no cover
    pass# pragma: no cover
 # pragma: no cover
sys.modules['Desktop'] = MockModule() # pragma: no cover
sys.modules['Desktop.test'] = MockModule() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(13699)

except ImportError:
    pass

