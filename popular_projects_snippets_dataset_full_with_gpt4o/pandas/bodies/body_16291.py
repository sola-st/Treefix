# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
s = Series(np.array([1.0, 1.0, 8.0]), dtype="i8")
assert s.dtype == np.dtype("i8")

msg = r"Cannot convert non-finite values \(NA or inf\) to integer"
with pytest.raises(IntCastingNaNError, match=msg):
    Series(np.array([1.0, 1.0, np.nan]), copy=True, dtype="i8")
