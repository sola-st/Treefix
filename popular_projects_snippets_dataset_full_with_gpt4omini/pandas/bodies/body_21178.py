# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/accessor.py
dtypes = data.dtypes
if not all(isinstance(t, SparseDtype) for t in dtypes):
    raise AttributeError(self._validation_msg)
