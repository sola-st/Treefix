import sys # pragma: no cover
import types # pragma: no cover

sys.modules['dir'] = types.ModuleType('dir') # pragma: no cover
sys.modules['dir.package'] = types.ModuleType('dir.package') # pragma: no cover
sys.modules['dir.package.module1'] = types.ModuleType('dir.package.module1') # pragma: no cover
sys.modules['dir.package.module1.foo'] = types.ModuleType('dir.package.module1.foo') # pragma: no cover

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

