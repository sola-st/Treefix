# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see gh-15832
# Updated: make sure we treat this list the same as we would treat
#  the equivalent ndarray
# GH#49599 pre-2.0 we silently retained float dtype, in 2.0 we raise
vals = [1, 2, 3.5]

msg = "Trying to coerce float values to integer"
with pytest.raises(ValueError, match=msg):
    Series(vals, dtype=any_int_numpy_dtype)
with pytest.raises(ValueError, match=msg):
    Series(np.array(vals), dtype=any_int_numpy_dtype)
