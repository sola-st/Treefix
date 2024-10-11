class DeprecatedClass:# pragma: no cover
    deprecated_class = 'DeprecatedClassName' # pragma: no cover
cls = DeprecatedClass # pragma: no cover
instance_warn_message = 'Warning: Class {cls} is deprecated. Use {new} instead.' # pragma: no cover
_clspath = lambda cls, path: f'{path}/{cls.__name__}' # pragma: no cover
old_class_path = 'path/to/old/class' # pragma: no cover
new_class = 'NewClassName' # pragma: no cover
new_class_path = 'path/to/new/class' # pragma: no cover
warn_category = DeprecationWarning # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover

class BaseClass:# pragma: no cover
    def __call__(self, *args, **kwargs):# pragma: no cover
        return 'Base call executed' # pragma: no cover
class DeprecatedClass(BaseClass):# pragma: no cover
    deprecated_class = 'DeprecatedClassName' # pragma: no cover
cls = DeprecatedClass.deprecated_class # pragma: no cover
instance_warn_message = 'Warning: Class {cls} is deprecated. Use {new} instead.' # pragma: no cover
_clspath = lambda cls, path: f'{path}/{cls}' # pragma: no cover
old_class_path = 'path/to/old/class' # pragma: no cover
new_class = 'NewClassName' # pragma: no cover
new_class_path = 'path/to/new/class' # pragma: no cover
warn_category = DeprecationWarning # pragma: no cover
args = () # pragma: no cover
kwargs = {} # pragma: no cover
instance = DeprecatedClass() # pragma: no cover

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
