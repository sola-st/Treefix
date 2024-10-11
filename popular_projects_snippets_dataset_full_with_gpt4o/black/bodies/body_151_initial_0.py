import token # pragma: no cover

self = type('Mock', (object,), {'leaves': [type('Leaf', (object,), {'type': token.STRING, 'value': '"""Example String"""'})()]})() # pragma: no cover
token.STRING = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is the line a triple quoted string?"""
aux = (
    bool(self)
    and self.leaves[0].type == token.STRING
    and self.leaves[0].value.startswith(('"""', "'''"))
)
_l_(16624)
exit(aux)
