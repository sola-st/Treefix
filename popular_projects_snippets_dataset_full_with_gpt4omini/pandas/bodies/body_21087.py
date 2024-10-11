# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
from pandas import value_counts

result = value_counts(self._ndarray, dropna=dropna).astype("Int64")
result.index = result.index.astype(self.dtype)
exit(result)
