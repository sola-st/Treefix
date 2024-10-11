from typing import List # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.leaves = ['single line', 'this is\na multiline string', 'another single line'] # pragma: no cover
def is_multiline_string(s: str) -> bool: return '\n' in s # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
aux = any(is_multiline_string(leaf) for leaf in self.leaves)
_l_(4157)
exit(aux)
