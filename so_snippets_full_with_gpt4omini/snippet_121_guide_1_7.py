import sys # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

sys.modules['dir'] = MagicMock() # pragma: no cover
sys.modules['dir.package'] = MagicMock() # pragma: no cover
sys.modules['dir.package.module1'] = MagicMock() # pragma: no cover
sys.modules['dir.package.module1'].foo = MagicMock() # pragma: no cover
sys.modules['dir.package.module2'] = MagicMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
#dir/package/module1/foo.py

#dir/package/module2/bar.py
from l3.Runtime import _l_
try:
    from ..module1 import foo
    _l_(2139)

except ImportError:
    pass

