class MyModule:# pragma: no cover
    def my_function(self):# pragma: no cover
        return 'Hello, World!'# pragma: no cover
# pragma: no cover
mymodule = MyModule() # pragma: no cover

import sys # pragma: no cover

class MockModule:# pragma: no cover
    pass# pragma: no cover
# pragma: no cover
sys.modules['mymodule'] = MockModule() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/684171/how-to-re-import-an-updated-package-while-in-python-interpreter
from l3.Runtime import _l_
del mymodule
_l_(73)
try:
    import mymodule
    _l_(75)

except ImportError:
    pass

