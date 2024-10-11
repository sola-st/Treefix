self = type('Mock', (object,), {'tolist': lambda self: [1, 2, 3]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
from l3.Runtime import _l_
"""
        Alias for tolist.
        """
aux = self.tolist()
_l_(15500)
exit(aux)
