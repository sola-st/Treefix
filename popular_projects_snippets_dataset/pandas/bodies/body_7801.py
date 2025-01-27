# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_nat.py
empty_index = index_without_na[:0]

index_with_na = index_without_na.copy(deep=True)
index_with_na._data[1] = NaT

assert empty_index._na_value is NaT
assert index_with_na._na_value is NaT
assert index_without_na._na_value is NaT

idx = index_without_na
assert idx._can_hold_na

tm.assert_numpy_array_equal(idx._isnan, np.array([False, False]))
assert idx.hasnans is False

idx = index_with_na
assert idx._can_hold_na

tm.assert_numpy_array_equal(idx._isnan, np.array([False, True]))
assert idx.hasnans is True
