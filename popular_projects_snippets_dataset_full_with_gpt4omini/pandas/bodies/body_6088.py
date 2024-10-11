# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# getitem[slice] should return an array
result = data[slice(0)]  # empty
assert isinstance(result, type(data))

result = data[slice(1)]  # scalar
assert isinstance(result, type(data))
