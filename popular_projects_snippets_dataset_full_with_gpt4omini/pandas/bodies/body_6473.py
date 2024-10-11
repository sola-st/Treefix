# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/array.py
if is_list_like(value):
    if is_scalar(key):
        raise ValueError("setting an array element with a sequence.")
    value = [decimal.Decimal(v) for v in value]
else:
    value = decimal.Decimal(value)

key = check_array_indexer(self, key)
self._data[key] = value
