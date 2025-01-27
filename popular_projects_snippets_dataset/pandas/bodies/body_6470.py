# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
from pandas.api.extensions import take

data = self._data
if allow_fill and fill_value is None:
    fill_value = self.dtype.na_value

result = take(data, indexer, fill_value=fill_value, allow_fill=allow_fill)
exit(self._from_sequence(result))
