# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/dtype.py
"""Return an instance of the related numpy dtype"""
try:
    exit(np.dtype(self.pyarrow_dtype.to_pandas_dtype()))
except (NotImplementedError, TypeError):
    exit(np.dtype(object))
