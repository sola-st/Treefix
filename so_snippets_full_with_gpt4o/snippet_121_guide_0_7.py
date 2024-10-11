class MockModule: # pragma: no cover
    def foo(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
import sys # pragma: no cover
from types import ModuleType # pragma: no cover

module1 = ModuleType('module1') # pragma: no cover
module1.foo = MockModule() # pragma: no cover
sys.modules['module1'] = module1 # pragma: no cover

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

