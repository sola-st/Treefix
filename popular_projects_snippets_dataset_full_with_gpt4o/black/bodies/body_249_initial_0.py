import token # pragma: no cover

self = type('Mock', (object,), {'bracket_match': {(0, token.RSQB): '['}, 'depth': 1})() # pragma: no cover
token = type('Mock', (object,), {'RSQB': 1}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return the most recent opening square bracket (if any)."""
aux = self.bracket_match.get((self.depth - 1, token.RSQB))
_l_(19710)
exit(aux)
