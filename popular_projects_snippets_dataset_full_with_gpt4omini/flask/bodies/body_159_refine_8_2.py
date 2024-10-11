from typing import Callable, Any # pragma: no cover

class MockObj: config = {'example_name': 'example_value'} # pragma: no cover
class MockSelf: __name__ = 'example_name'; get_converter = None # pragma: no cover
obj = MockObj() # pragma: no cover
self = MockSelf() # pragma: no cover

from typing import Callable, Dict # pragma: no cover

class MockObj: config = {'example_name': 'example_value'} # pragma: no cover
obj = MockObj() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
if obj is None:
    _l_(8938)

    aux = self
    _l_(8937)
    exit(aux)
rv = obj.config[self.__name__]
_l_(8939)
if self.get_converter is not None:
    _l_(8941)

    rv = self.get_converter(rv)
    _l_(8940)
aux = rv
_l_(8942)
exit(aux)
