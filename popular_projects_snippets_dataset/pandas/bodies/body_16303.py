# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 22585
# Updated: make sure we treat this list the same as we would treat the
# equivalent ndarray
vals = [1, 2, np.nan]
# pre-2.0 this would return with a float dtype, in 2.0 we raise

msg = "cannot convert float NaN to integer"
with pytest.raises(ValueError, match=msg):
    Series(vals, dtype=any_int_numpy_dtype)
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    Series(np.array(vals), dtype=any_int_numpy_dtype)
