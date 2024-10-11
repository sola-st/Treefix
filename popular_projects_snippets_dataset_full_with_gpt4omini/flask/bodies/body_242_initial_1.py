from typing import List, Callable # pragma: no cover

value = 15 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert a value to a tagged representation if necessary."""
for tag in self.order:
    _l_(9225)

    if tag.check(value):
        _l_(9224)

        aux = tag.tag(value)
        _l_(9223)
        exit(aux)
aux = value
_l_(9226)

exit(aux)
