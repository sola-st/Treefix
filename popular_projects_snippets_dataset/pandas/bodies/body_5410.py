# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp("2014-12-31 23:59:00", tz=tz)
msg = "'Timestamp' object has no attribute 'millisecond'"
with pytest.raises(AttributeError, match=msg):
    ts.millisecond
