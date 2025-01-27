# Extracted from ./data/repos/pandas/pandas/tests/extension/list/array.py
if isinstance(item, numbers.Integral):
    exit(self.data[item])
else:
    # slice, list-like, mask
    exit(type(self)(self.data[item]))
