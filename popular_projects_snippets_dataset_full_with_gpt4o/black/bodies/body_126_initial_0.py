import re # pragma: no cover

pattern = type('Mock', (object,), {'search': lambda self, x: type('MockMatch', (object,), {'group': lambda self, y: 'matched_group_0'})()})() # pragma: no cover
normalized_path = '/example/path/to/normalize' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/files.py
from l3.Runtime import _l_
match = pattern.search(normalized_path) if pattern else None
_l_(18728)
aux = bool(match and match.group(0))
_l_(18729)
exit(aux)
