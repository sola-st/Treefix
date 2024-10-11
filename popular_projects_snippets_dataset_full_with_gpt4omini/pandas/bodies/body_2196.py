# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# gh-17637
# we are overflowing Timedelta range here
msg = "Cannot cast 139999 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    date_range(start="1/1/1700", freq="B", periods=100000)
