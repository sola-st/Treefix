# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
rng = date_range("1/1/2011", periods=10, freq="H")
ser = Series(np.random.randn(len(rng)), index=rng)

ser_utc = ser.tz_localize("utc")

msg = "Cannot join tz-naive with tz-aware DatetimeIndex"
with pytest.raises(Exception, match=msg):
    ser + ser_utc

with pytest.raises(Exception, match=msg):
    ser_utc + ser
