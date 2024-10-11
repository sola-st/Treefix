from typing import Type, Any # pragma: no cover

http_method_funcs = ['GET', 'POST', 'PUT', 'DELETE'] # pragma: no cover
class Base: pass # pragma: no cover
class Mock(Base): pass # pragma: no cover
class MyClass(Mock): pass # pragma: no cover
cls = MyClass # pragma: no cover
kwargs = {} # pragma: no cover

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
