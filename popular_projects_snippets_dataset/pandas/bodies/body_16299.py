# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see gh-15832
msg = "Trying to coerce negative values to unsigned integers"
with pytest.raises(OverflowError, match=msg):
    Series([-1], dtype=any_unsigned_int_numpy_dtype)
