# pragma: no cover
    if not isinstance(node, str):# pragma: no cover
        return False# pragma: no cover
    # pragma: no cover
    return bool(inspect.isbuiltin(eval(node))) or bool(inspect.ismodule(eval(node)))# pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), {'leaves': ['']})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Is this an import line?"""
aux = bool(self) and is_import(self.leaves[0])
_l_(17761)
exit(aux)
