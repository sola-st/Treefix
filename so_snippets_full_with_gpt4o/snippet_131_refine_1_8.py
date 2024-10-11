from pathlib import Path # pragma: no cover
import sys # pragma: no cover

__file__ = 'dummy_file_path.py' # pragma: no cover
sys = type('MockSys', (object,), {'path': sys.path}) # pragma: no cover
sys.path = [] # pragma: no cover

from pathlib import Path # pragma: no cover
import sys # pragma: no cover

__file__ = 'dummy_file_path.py' # pragma: no cover
class MockSysPath(list):# pragma: no cover
    pass# pragma: no cover
sys = type('MockSys', (object,), {'path': MockSysPath()}) # pragma: no cover
mock_module = type('MockModule', (object,), {})()# pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
## Standalone boilerplate before relative imports
from l3.Runtime import _l_
if __package__ is None:
    _l_(12702)

    DIR = Path(__file__).resolve().parent
    _l_(12699)
    sys.path.insert(0, str(DIR.parent))
    _l_(12700)
    __package__ = DIR.name
    _l_(12701)
try:
    from . import variable_in__init__py
    _l_(12704)

except ImportError:
    pass
try:
    from . import other_module_in_package
    _l_(12706)

except ImportError:
    pass

