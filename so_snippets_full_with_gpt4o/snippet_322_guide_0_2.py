import types # pragma: no cover

Mock = type('Mock', (object,), {'test': types.ModuleType('Mock.test')}) # pragma: no cover
sys.modules['Desktop'] = Mock # pragma: no cover
sys.modules['Desktop.test'] = Mock.test # pragma: no cover
setattr(Mock.test, 'attribute', 'some_value') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path
from l3.Runtime import _l_
try:
    from Desktop.test import *
    _l_(13699)

except ImportError:
    pass

