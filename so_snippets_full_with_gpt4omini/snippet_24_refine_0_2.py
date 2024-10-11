import os # pragma: no cover
import sys # pragma: no cover
import cheese # pragma: no cover

__file__ = 'path/to/your/script.py' # pragma: no cover

import os # pragma: no cover
import sys # pragma: no cover
import cheese # pragma: no cover
class vehicle_parts: pass # pragma: no cover

__file__ = 'path/to/your/script.py' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/448271/what-is-init-py-for
from l3.Runtime import _l_
try:
    import os
    _l_(36)

except ImportError:
    pass
try:
    import sys
    _l_(38)

except ImportError:
    pass
dir_path = os.path.dirname(__file__)
_l_(39)
sys.path.insert(0, dir_path)
_l_(40)
try:
    import cheese
    _l_(42)

except ImportError:
    pass
try:
    from vehicle_parts import *
    _l_(44)

except ImportError:
    pass
# etc.

