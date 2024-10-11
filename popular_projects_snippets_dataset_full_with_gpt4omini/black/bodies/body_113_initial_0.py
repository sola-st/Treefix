idx = 0 # pragma: no cover
seq = [1, 2, 3] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Returns:
            True iff @idx is positive AND seq[@idx] does NOT raise an
            IndexError.
        """
aux = 0 <= idx < len(seq)
_l_(4594)
exit(aux)
