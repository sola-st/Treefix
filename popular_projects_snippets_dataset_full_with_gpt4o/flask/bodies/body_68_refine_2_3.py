import types # pragma: no cover

kwargs = {} # pragma: no cover
cls = type('MockClass', (object,), {'__dict__': {}, '__bases__': (), 'methods': set()}) # pragma: no cover
http_method_funcs = [] # pragma: no cover

from typing import Any, Type # pragma: no cover

http_method_funcs = ['get', 'post', 'put', 'delete'] # pragma: no cover
class BaseClass: # pragma: no cover
    methods = set() # pragma: no cover
class MockClass(BaseClass): # pragma: no cover
    pass # pragma: no cover
cls: Type[MockClass] = MockClass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/views.py
from l3.Runtime import _l_
super().__init_subclass__(**kwargs)
_l_(16190)

if "methods" not in cls.__dict__:
    _l_(16200)

    methods = set()
    _l_(16191)

    for base in cls.__bases__:
        _l_(16194)

        if getattr(base, "methods", None):
            _l_(16193)

            methods.update(base.methods)  # type: ignore[attr-defined]
            _l_(16192)  # type: ignore[attr-defined]

    for key in http_method_funcs:
        _l_(16197)

        if hasattr(cls, key):
            _l_(16196)

            methods.add(key.upper())
            _l_(16195)

    if methods:
        _l_(16199)

        cls.methods = methods
        _l_(16198)
