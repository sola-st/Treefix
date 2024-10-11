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
_l_(16929)
aux = self.data.memory_usage(index=True, deep=deep)
_l_(16930)
exit(aux)
