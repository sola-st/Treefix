# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
if not isinstance(data.dtype, SparseDtype):
    raise AttributeError(self._validation_msg)
