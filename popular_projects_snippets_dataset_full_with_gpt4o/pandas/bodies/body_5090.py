# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
ts = Timestamp("1700-01-01").as_unit("ns")
msg = "Cannot cast 259987 from D to 'ns' without overflow."
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    ts + Timedelta(13 * 19999, unit="D")

msg = "Cannot cast 259987 days 00:00:00 to unit='ns' without overflow"
with pytest.raises(OutOfBoundsTimedelta, match=msg):
    ts + timedelta(days=13 * 19999)
