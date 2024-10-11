import inspect # pragma: no cover

class DeprecatedClass: # pragma: no cover
    deprecated_class = type('DeprecatedClassType', (object,), {}) # pragma: no cover
 # pragma: no cover
class NewClass: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
class MockSuperClass: # pragma: no cover
    @staticmethod # pragma: no cover
    def __subclasscheck__(subclass): # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
super = lambda: MockSuperClass # pragma: no cover
cls = type('OtherClass', (MockSuperClass,), {}) # pragma: no cover
sub = DeprecatedClass.deprecated_class # pragma: no cover
new_class = NewClass # pragma: no cover

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
