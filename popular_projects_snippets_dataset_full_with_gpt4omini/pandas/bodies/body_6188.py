# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
data2 = type(data)._from_sequence([data[0]] * len(data), dtype=data.dtype)
data_na = type(data)._from_sequence([na_value] * len(data), dtype=data.dtype)

data = tm.box_expected(data, box, transpose=False)
data2 = tm.box_expected(data2, box, transpose=False)
data_na = tm.box_expected(data_na, box, transpose=False)

# we are asserting with `is True/False` explicitly, to test that the
# result is an actual Python bool, and not something "truthy"

assert data.equals(data) is True
assert data.equals(data.copy()) is True

# unequal other data
assert data.equals(data2) is False
assert data.equals(data_na) is False

# different length
assert data[:2].equals(data[:3]) is False

# empty are equal
assert data[:0].equals(data[:0]) is True

# other types
assert data.equals(None) is False
assert data[[0]].equals(data[0]) is False
