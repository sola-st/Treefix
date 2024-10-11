# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
msg = r"Cannot convert non-finite values \(NA or inf\) to integer"

with pytest.raises(IntCastingNaNError, match=msg):
    DataFrame([[np.nan, 1], [1, 0]], dtype=np.int64)
