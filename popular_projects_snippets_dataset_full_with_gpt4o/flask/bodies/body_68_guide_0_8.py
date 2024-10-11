from typing import Any # pragma: no cover

class MockBase:# pragma: no cover
    methods = {'GET'}# pragma: no cover
    def __new__(cls, *args, **kwargs):# pragma: no cover
        instance = super(MockBase, cls).__new__(cls)# pragma: no cover
        return instance # pragma: no cover
http_method_funcs = {'get': lambda x: x} # pragma: no cover
kwargs = {} # pragma: no cover
cls = type('Mock', (MockBase,), {}) # pragma: no cover

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
