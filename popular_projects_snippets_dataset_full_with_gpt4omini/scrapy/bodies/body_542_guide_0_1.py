type # pragma: no cover

class DeprecatedClass:  # Mocking the DeprecatedClass# pragma: no cover
    deprecated_class = 'DeprecatedClass' # pragma: no cover
class NewClass:  # A new class to represent 'new'# pragma: no cover
    pass # pragma: no cover
instance_warn_message = '{cls} is deprecated; use {new} instead.' # pragma: no cover
warn_category = UserWarning # pragma: no cover
cls = DeprecatedClass.deprecated_class # pragma: no cover
old_class_path = 'path.to.DeprecatedClass' # pragma: no cover
new_class = NewClass # pragma: no cover
new_class_path = 'path.to.NewClass' # pragma: no cover
args = [] # pragma: no cover
kwargs = {} # pragma: no cover
super = type('MockSuper', (object,), {'__call__': lambda self, *args, **kwargs: 'called'}) # pragma: no cover

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
