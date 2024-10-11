from typing import Set, Type, Any # pragma: no cover

kwargs = {} # pragma: no cover
cls = type('MockClass', (object,), {'__dict__': {}, '__bases__': (object,), 'methods': None}) # pragma: no cover
http_method_funcs = {'get', 'post', 'put', 'delete'} # pragma: no cover

from typing import Dict, Set, Any # pragma: no cover

class BaseClass: pass # pragma: no cover
class MockClass(BaseClass):# pragma: no cover
    def __init_subclass__(cls, **kwargs): pass # pragma: no cover
kwargs = {'arg1': 'value1'} # pragma: no cover
cls = MockClass # pragma: no cover
http_method_funcs = ['get', 'post'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/views.py
from l3.Runtime import _l_
super().__init_subclass__(**kwargs)
_l_(4503)

if "methods" not in cls.__dict__:
    _l_(4513)

    methods = set()
    _l_(4504)

    for base in cls.__bases__:
        _l_(4507)

        if getattr(base, "methods", None):
            _l_(4506)

            methods.update(base.methods)  # type: ignore[attr-defined]
            _l_(4505)  # type: ignore[attr-defined]

    for key in http_method_funcs:
        _l_(4510)

        if hasattr(cls, key):
            _l_(4509)

            methods.add(key.upper())
            _l_(4508)

    if methods:
        _l_(4512)

        cls.methods = methods
        _l_(4511)
