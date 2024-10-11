from typing import Any, Callable, Dict # pragma: no cover

self = type('Mock', (), {'__name__': 'mock_name', 'get_converter': None})() # pragma: no cover
obj = type('Mock', (), {'config': {'mock_name': 42}})() # pragma: no cover

from typing import Optional, Callable # pragma: no cover

class MockConfig: config = {'example_name': 'example_value'} # pragma: no cover
class Mock: __name__ = 'example_name'; get_converter: Optional[Callable[[str], str]] = None # pragma: no cover
obj = type('MockObj', (object,), {'config': MockConfig.config})() # pragma: no cover
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
