# Extracted from ./data/repos/pandas/pandas/core/nanops.py
super().__init__()
self.dtypes = tuple(pandas_dtype(dtype).type for dtype in dtypes)
