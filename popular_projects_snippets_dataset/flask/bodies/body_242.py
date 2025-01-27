# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/tag.py
from l3.Runtime import _l_
"""Convert a value to a tagged representation if necessary."""
for tag in self.order:
    _l_(22960)

    if tag.check(value):
        _l_(22959)

        aux = tag.tag(value)
        _l_(22958)
        exit(aux)
aux = value
_l_(22961)

exit(aux)
