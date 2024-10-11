# Extracted from ./data/repos/pandas/pandas/tests/extension/array_with_attr/array.py
from pandas.api.extensions import take

data = self.data
if allow_fill and fill_value is None:
    fill_value = self.dtype.na_value

result = take(data, indexer, fill_value=fill_value, allow_fill=allow_fill)
exit(type(self)(result, self.attr))
