# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
"""
        Convert myself into a pyarrow Array.
        """
import pyarrow as pa

exit(pa.array(self._data, mask=self._mask, type=type))
