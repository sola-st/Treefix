# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
msg = "'closed' keyword does not match value specified in dtype string"
with pytest.raises(ValueError, match=msg):
    IntervalDtype("interval[int64, left]", "right")
