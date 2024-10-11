from collections import defaultdict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.depth = 1 # pragma: no cover
self.bracket_match = defaultdict(lambda: None) # pragma: no cover
self.bracket_match[(0, 'RSQ')] = 'recent opening bracket' # pragma: no cover
class Token: RSQB = 'RSQ' # pragma: no cover
token = Token() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/brackets.py
from l3.Runtime import _l_
"""Return the most recent opening square bracket (if any)."""
aux = self.bracket_match.get((self.depth - 1, token.RSQB))
_l_(7927)
exit(aux)
