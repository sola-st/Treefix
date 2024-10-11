class Base: methods = set() # pragma: no cover
class MockMeta(type):# pragma: no cover
    def __init__(cls, name, bases, attrs):# pragma: no cover
        super().__init__(name, bases, attrs)# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def __init_subclass__(cls, **kwargs):# pragma: no cover
        super().__init_subclass__(**kwargs)# pragma: no cover
# pragma: no cover
http_method_funcs = ['get', 'post', 'put', 'delete'] # pragma: no cover
kwargs = {} # pragma: no cover
cls = MockMeta('MyClass', (Base,), {}) # pragma: no cover

from typing import Dict, Set, Any # pragma: no cover

kwargs = {} # pragma: no cover
class Base: pass # pragma: no cover
class MockMeta(type):# pragma: no cover
    def __init__(cls, name: str, bases: tuple, attrs: Dict[str, Any]):# pragma: no cover
        super().__init__(name, bases, attrs)# pragma: no cover
# pragma: no cover
    @classmethod# pragma: no cover
    def __init_subclass__(cls, **kwargs):# pragma: no cover
        super().__init_subclass__(**kwargs) # pragma: no cover
class MockClass(metaclass=MockMeta): pass # pragma: no cover
cls = MockClass # pragma: no cover
http_method_funcs = ['GET', 'POST', 'PUT', 'DELETE'] # pragma: no cover

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
