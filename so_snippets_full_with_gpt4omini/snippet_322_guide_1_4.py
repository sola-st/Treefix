import sys # pragma: no cover
class Mock: pass # pragma: no cover

sys.modules['Desktop'] = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(2264)

except ImportError:
    pass

