from typing import List # pragma: no cover
def is_import(item): return item in {'module1', 'module2'} # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.leaves = ['module1'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(6269)
exit(aux)
