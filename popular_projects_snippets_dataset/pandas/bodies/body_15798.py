# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# gh-14265: check NaN and inf raise error when converting to int
msg = "Cannot convert non-finite values \\(NA or inf\\) to integer"
ser = Series([value])

with pytest.raises(ValueError, match=msg):
    ser.astype(dtype)
