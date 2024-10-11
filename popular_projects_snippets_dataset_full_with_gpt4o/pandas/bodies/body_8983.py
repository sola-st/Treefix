# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
arr = SparseArray([1.0, np.nan, 2.0], fill_value=np.nan)
arr.fill_value = 2
assert arr.fill_value == 2

arr = SparseArray([1, 0, 2], fill_value=0, dtype=np.int64)
arr.fill_value = 2
assert arr.fill_value == 2

# TODO: this seems fine? You can construct an integer
# sparsearray with NaN fill value, why not update one?
# coerces to int
# msg = "unable to set fill_value 3\\.1 to int64 dtype"
# with pytest.raises(ValueError, match=msg):
arr.fill_value = 3.1
assert arr.fill_value == 3.1

# msg = "unable to set fill_value nan to int64 dtype"
# with pytest.raises(ValueError, match=msg):
arr.fill_value = np.nan
assert np.isnan(arr.fill_value)

arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool_)
arr.fill_value = True
assert arr.fill_value

# FIXME: don't leave commented-out
# coerces to bool
# TODO: we can construct an sparse array of bool
#      type and use as fill_value any value
# msg = "fill_value must be True, False or nan"
# with pytest.raises(ValueError, match=msg):
#    arr.fill_value = 0

# msg = "unable to set fill_value nan to bool dtype"
# with pytest.raises(ValueError, match=msg):
arr.fill_value = np.nan
assert np.isnan(arr.fill_value)
