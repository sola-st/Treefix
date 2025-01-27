# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/scrapy/scrapy/utils/deprecate.py
from l3.Runtime import _l_
old = DeprecatedClass.deprecated_class
_l_(17438)
if cls is old:
    _l_(17441)

    msg = instance_warn_message.format(cls=_clspath(cls, old_class_path),
                                       new=_clspath(new_class, new_class_path))
    _l_(17439)
    warnings.warn(msg, warn_category, stacklevel=2)
    _l_(17440)
aux = super().__call__(*args, **kwargs)
_l_(17442)
exit(aux)
