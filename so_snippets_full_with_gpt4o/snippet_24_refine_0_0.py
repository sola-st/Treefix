import os # pragma: no cover

__file__ = os.path.abspath('script.py') # pragma: no cover

import os # pragma: no cover
import sys # pragma: no cover
import types # pragma: no cover

__file__ = os.path.abspath('script.py') # pragma: no cover
sys.modules['cheese'] = types.ModuleType('cheese') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/448271/what-is-init-py-for
from l3.Runtime import _l_
try:
    import os
    _l_(11871)

except ImportError:
    pass
try:
    import sys
    _l_(11873)

except ImportError:
    pass
dir_path = os.path.dirname(__file__)
_l_(11874)
sys.path.insert(0, dir_path)
_l_(11875)
try:
    import cheese
    _l_(11877)

except ImportError:
    pass
try:
    from vehicle_parts import *
    _l_(11879)

except ImportError:
    pass
# etc.

