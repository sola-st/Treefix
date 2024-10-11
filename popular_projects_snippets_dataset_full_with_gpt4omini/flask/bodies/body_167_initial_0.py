from typing import Dict, Any # pragma: no cover

t = type('Mock', (), {'Dict': Dict, 'Any': Any}) # pragma: no cover
mapping = {'KEY1': 'value1', 'KEY2': 'value2'} # pragma: no cover
kwargs = {'key3': 'value3', 'key4': 'value4'} # pragma: no cover
self = {} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/config.py
from l3.Runtime import _l_
"""Updates the config like :meth:`update` ignoring items with
        non-upper keys.

        :return: Always returns ``True``.

        .. versionadded:: 0.11
        """
mappings: t.Dict[str, t.Any] = {}
_l_(8327)
if mapping is not None:
    _l_(8329)

    mappings.update(mapping)
    _l_(8328)
mappings.update(kwargs)
_l_(8330)
for key, value in mappings.items():
    _l_(8333)

    if key.isupper():
        _l_(8332)

        self[key] = value
        _l_(8331)
aux = True
_l_(8334)
exit(aux)
