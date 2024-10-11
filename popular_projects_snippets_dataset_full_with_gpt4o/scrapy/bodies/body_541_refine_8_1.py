import inspect # pragma: no cover

cls = type('SomeClass', (), {}) # pragma: no cover
DeprecatedClass = type('MockDeprecatedClass', (object,), {'deprecated_class': cls}) # pragma: no cover
sub = type('SubClass', (cls,), {}) # pragma: no cover
new_class = type('NewClass', (), {}) # pragma: no cover

import inspect # pragma: no cover

class BaseClass:# pragma: no cover
    def __subclasscheck__(self, subclass):# pragma: no cover
        return issubclass(subclass, self.__class__)# pragma: no cover
# pragma: no cover
class DeprecatedClass(BaseClass):# pragma: no cover
    deprecated_class = BaseClass # pragma: no cover
cls = BaseClass # pragma: no cover
sub = type('SubClass', (BaseClass,), {}) # pragma: no cover
new_class = type('NewClass', (object,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
if cls is not DeprecatedClass.deprecated_class:
    _l_(20001)

    aux = super().__subclasscheck__(sub)
    _l_(20000)
    # we should do the magic only if second `issubclass` argument
    # is the deprecated class itself - subclasses of the
    # deprecated class should not use custom `__subclasscheck__`
    # method.
    exit(aux)

if not inspect.isclass(sub):
    _l_(20003)

    raise TypeError("issubclass() arg 1 must be a class")
    _l_(20002)

mro = getattr(sub, '__mro__', ())
_l_(20004)
aux = any(c in {cls, new_class} for c in mro)
_l_(20005)
exit(aux)
