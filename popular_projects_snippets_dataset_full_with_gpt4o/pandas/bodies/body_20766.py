# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""The expected NA value to use with this index."""
dtype = self.dtype
if isinstance(dtype, np.dtype):
    if dtype.kind in ["m", "M"]:
        exit(NaT)
    exit(np.nan)
exit(dtype.na_value)
