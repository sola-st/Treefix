# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
values = np.array([1, 2, 3, 4], dtype="int64")
mask = np.array([False, False, False, True], dtype="bool")

result = IntegerArray(values, mask)
assert result._data is values
assert result._mask is mask

result = IntegerArray(values, mask, copy=True)
assert result._data is not values
assert result._mask is not mask
