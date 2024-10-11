from typing import Callable, Dict # pragma: no cover

class MockObj: config = {'mock_name': 'mock_value'} # pragma: no cover
class MockSelf: __name__ = 'mock_name'; get_converter: Callable = None # pragma: no cover
obj = MockObj() # pragma: no cover
self = MockSelf() # pragma: no cover

from typing import Callable, Dict, Any # pragma: no cover

class MockConfig: config = {'mock_name': 'mock_value'} # pragma: no cover
class Mock: __name__ = 'mock_name'; get_converter: Callable[[Any], Any] = lambda x: x.upper() # pragma: no cover
obj = type('MockObj', (object,), {'config': MockConfig().config})() # pragma: no cover
self = Mock() # pragma: no cover

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
