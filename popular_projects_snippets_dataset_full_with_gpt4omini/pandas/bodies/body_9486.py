# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
values = np.array([True, False, True, False], dtype="bool")
mask = np.array([False, False, False, True], dtype="bool")

result = BooleanArray(values, mask)
assert result._data is values
assert result._mask is mask

result = BooleanArray(values, mask, copy=True)
assert result._data is not values
assert result._mask is not mask
