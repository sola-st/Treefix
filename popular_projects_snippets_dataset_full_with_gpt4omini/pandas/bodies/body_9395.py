# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
all_data = all_data[:10]

ints = all_data[~all_data.isna()]
mixed = all_data
dtype = Int8Dtype()

# coerce to same type - ints
s = pd.Series(ints)
result = s.astype(all_data.dtype)
expected = pd.Series(ints)
tm.assert_series_equal(result, expected)

# coerce to same other - ints
s = pd.Series(ints)
result = s.astype(dtype)
expected = pd.Series(ints, dtype=dtype)
tm.assert_series_equal(result, expected)

# coerce to same numpy_dtype - ints
s = pd.Series(ints)
result = s.astype(all_data.dtype.numpy_dtype)
expected = pd.Series(ints._data.astype(all_data.dtype.numpy_dtype))
tm.assert_series_equal(result, expected)

# coerce to same type - mixed
s = pd.Series(mixed)
result = s.astype(all_data.dtype)
expected = pd.Series(mixed)
tm.assert_series_equal(result, expected)

# coerce to same other - mixed
s = pd.Series(mixed)
result = s.astype(dtype)
expected = pd.Series(mixed, dtype=dtype)
tm.assert_series_equal(result, expected)

# coerce to same numpy_dtype - mixed
s = pd.Series(mixed)
msg = "cannot convert NA to integer"
with pytest.raises(ValueError, match=msg):
    s.astype(all_data.dtype.numpy_dtype)

# coerce to object
s = pd.Series(mixed)
result = s.astype("object")
expected = pd.Series(np.asarray(mixed))
tm.assert_series_equal(result, expected)
