# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
values = np.array([1, 2, 3, 4], dtype="float64")
mask = np.array([False, False, False, True], dtype="bool")

result = FloatingArray(values, mask)
assert result._data is values
assert result._mask is mask

result = FloatingArray(values, mask, copy=True)
assert result._data is not values
assert result._mask is not mask
