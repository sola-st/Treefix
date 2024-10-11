import token # pragma: no cover

self = type('Mock', (object,), {'leaves': [type('Leaf', (object,), {'type': token.NAME, 'value': 'class'})()]})() # pragma: no cover
token = type('MockToken', (object,), {'NAME': 1}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this line a class definition?"""
aux = (
    bool(self)
    and self.leaves[0].type == token.NAME
    and self.leaves[0].value == "class"
)
_l_(17753)
exit(aux)
