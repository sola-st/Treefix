import pandas as pd # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self.memory_usage = 'deep' # pragma: no cover
self.data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
from l3.Runtime import _l_
"""Memory usage in bytes.

        Returns
        -------
        memory_usage_bytes : int
            Object's total memory usage in bytes.
        """
deep = self.memory_usage == "deep"
_l_(6728)
aux = self.data.memory_usage(index=True, deep=deep)
_l_(6729)
exit(aux)
