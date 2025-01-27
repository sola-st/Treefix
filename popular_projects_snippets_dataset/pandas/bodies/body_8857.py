# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
a = DatetimeArray(pd.date_range("2000", periods=2, freq="D", tz="US/Central"))
a[0] = pd.Timestamp("2000", tz="US/Central")
assert a.freq is None
