import sys # pragma: no cover

sys.modules['dir'] = type('Mock', (object,), {})() # pragma: no cover
sys.modules['dir.package'] = type('Mock', (object,), {})() # pragma: no cover
sys.modules['dir.package.module1'] = type('Mock', (object,), {})() # pragma: no cover
sys.modules['dir.package.module1'].foo = None # pragma: no cover
sys.modules['dir.package.module2'] = type('Mock', (object,), {})() # pragma: no cover
sys.modules['dir.package.module2'].bar = None # pragma: no cover

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

