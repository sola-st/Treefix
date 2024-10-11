import warnings # pragma: no cover
class DeprecatedClass: pass # pragma: no cover
def _clspath(cls, path): return f'{cls.__module__}.{cls.__name__}' # pragma: no cover
new_class = type('NewClass', (), {}) # pragma: no cover

old_class_path = 'path.to.OldClass' # pragma: no cover
new_class_path = 'path.to.NewClass' # pragma: no cover
cls = DeprecatedClass # pragma: no cover
instance_warn_message = 'The class {cls} is deprecated. Use {new} instead.' # pragma: no cover
warn_category = DeprecationWarning # pragma: no cover
instance = DeprecatedClass() # pragma: no cover
super = type('MockSuper', (object,), {'__call__': lambda self, *args, **kwargs: 'success'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
old = DeprecatedClass.deprecated_class
_l_(6006)
if cls is old:
    _l_(6009)

    msg = instance_warn_message.format(cls=_clspath(cls, old_class_path),
                                       new=_clspath(new_class, new_class_path))
    _l_(6007)
    warnings.warn(msg, warn_category, stacklevel=2)
    _l_(6008)
aux = super().__call__(*args, **kwargs)
_l_(6010)
exit(aux)
