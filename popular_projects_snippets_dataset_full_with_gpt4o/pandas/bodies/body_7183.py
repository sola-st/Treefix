# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py

# see gh-15832
msg = "Trying to coerce negative values to unsigned integers"

with pytest.raises(OverflowError, match=msg):
    Index([-1], dtype=any_unsigned_int_numpy_dtype)
