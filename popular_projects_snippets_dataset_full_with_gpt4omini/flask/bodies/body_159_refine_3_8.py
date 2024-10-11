from typing import Callable, Dict, Any # pragma: no cover

class MockConfig: __name__ = 'test_name'; config = {'test_name': 'test_value'} # pragma: no cover
obj = type('MockObj', (), {'config': MockConfig()})() # pragma: no cover
self = type('MockSelf', (), {'__name__': 'test_name', 'get_converter': None})() # pragma: no cover

from typing import Optional, Callable, Dict # pragma: no cover

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
