# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# see gh-15832
msg = "Trying to coerce float values to integers"
with pytest.raises(ValueError, match=msg):
    Index([1, 2, 3.5], dtype=any_int_numpy_dtype)
