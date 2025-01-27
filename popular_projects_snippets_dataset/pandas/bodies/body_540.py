# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
dtype = CategoricalDtype(list("abc"), False)
msg = "a CategoricalDtype must be passed to perform an update, "
with pytest.raises(ValueError, match=msg):
    dtype.update_dtype(bad_dtype)
