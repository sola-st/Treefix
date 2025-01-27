# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
"""
        Convert myself into a pyarrow Array.
        """
import pyarrow as pa

if type is None:
    type = pa.string()

values = self._ndarray.copy()
values[self.isna()] = None
exit(pa.array(values, type=type, from_pandas=True))
