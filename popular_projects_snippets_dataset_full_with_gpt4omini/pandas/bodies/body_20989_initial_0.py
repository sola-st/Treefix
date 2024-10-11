class Mock:# pragma: no cover
    def tolist(self):# pragma: no cover
        return []# pragma: no cover
# pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
from l3.Runtime import _l_
"""
        Alias for tolist.
        """
aux = self.tolist()
_l_(4208)
exit(aux)
