# Extracted from ./data/repos/pandas/pandas/io/stata.py
self.fmtlist: list[str] = []
self.typlist: list[int] = []
for col, dtype in dtypes.items():
    self.fmtlist.append(_dtype_to_default_stata_fmt(dtype, self.data[col]))
    self.typlist.append(_dtype_to_stata_type(dtype, self.data[col]))
