# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
idx1 = date_range("2001", periods=5, freq="H", tz="US/Eastern")
ser = Series(np.random.randn(len(idx1)), index=idx1)
ser_central = ser.tz_convert("US/Central")
# different timezones convert to UTC

new1, new2 = ser.align(ser_central)
assert new1.index.tz is timezone.utc
assert new2.index.tz is timezone.utc
