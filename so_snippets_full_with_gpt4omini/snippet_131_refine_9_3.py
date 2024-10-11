from pathlib import Path # pragma: no cover
import sys # pragma: no cover

Path = Path # pragma: no cover
__file__ = 'path/to/your/script.py' # pragma: no cover
sys = sys # pragma: no cover
sys.path = type('Mock', (object,), {'path': []})() # pragma: no cover

from pathlib import Path # pragma: no cover
import sys # pragma: no cover

Path = type('MockPath', (object,), {'resolve': lambda self: self, 'parent': None})() # pragma: no cover
__file__ = 'path/to/mock_file.py' # pragma: no cover
sys = type('MockSys', (object,), {'path': []})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
## Standalone boilerplate before relative imports
from l3.Runtime import _l_
if __package__ is None:
    _l_(1040)

    DIR = Path(__file__).resolve().parent
    _l_(1037)
    sys.path.insert(0, str(DIR.parent))
    _l_(1038)
    __package__ = DIR.name
    _l_(1039)
try:
    from . import variable_in__init__py
    _l_(1042)

except ImportError:
    pass
try:
    from . import other_module_in_package
    _l_(1044)

except ImportError:
    pass

