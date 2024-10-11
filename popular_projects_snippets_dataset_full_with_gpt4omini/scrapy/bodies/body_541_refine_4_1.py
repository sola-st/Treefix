class DeprecatedClass:# pragma: no cover
    pass
sub = type('NewClass', (), {}) # pragma: no cover
new_class = type('NewClass', (object,), {}) # pragma: no cover

import inspect # pragma: no cover

class DeprecatedClass:# pragma: no cover
    deprecated_class = object # pragma: no cover
cls = DeprecatedClass.deprecated_class # pragma: no cover
sub = type('DummyClass', (object,), {}) # pragma: no cover
new_class = type('NewClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
if cls is not DeprecatedClass.deprecated_class:
    _l_(8951)

    aux = super().__subclasscheck__(sub)
    _l_(8950)
    # we should do the magic only if second `issubclass` argument
    # is the deprecated class itself - subclasses of the
    # deprecated class should not use custom `__subclasscheck__`
    # method.
    exit(aux)

if not inspect.isclass(sub):
    _l_(8953)

    raise TypeError("issubclass() arg 1 must be a class")
    _l_(8952)

mro = getattr(sub, '__mro__', ())
_l_(8954)
aux = any(c in {cls, new_class} for c in mro)
_l_(8955)
exit(aux)
