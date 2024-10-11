import sys # pragma: no cover
import types # pragma: no cover
import os # pragma: no cover

sys.modules['dir.package.module1'] = types.ModuleType('module1') # pragma: no cover
sys.modules['dir.package.module1.foo'] = types.ModuleType('foo') # pragma: no cover
sys.modules['dir.package'] = types.ModuleType('package') # pragma: no cover
sys.modules['dir.package.module2'] = types.ModuleType('module2') # pragma: no cover
sys.modules['dir.package.module2.bar'] = types.ModuleType('bar') # pragma: no cover
os.makedirs('dir/package/module1', exist_ok=True) # pragma: no cover
os.makedirs('dir/package/module2', exist_ok=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
#dir/package/module1/foo.py

#dir/package/module2/bar.py
from l3.Runtime import _l_
try:
    from ..module1 import foo
    _l_(14327)

except ImportError:
    pass

