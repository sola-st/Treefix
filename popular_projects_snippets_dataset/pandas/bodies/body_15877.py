# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
idx = pd.date_range("2016-01-01", periods=5, tz="US/Pacific")
if as_period:
    idx = idx.tz_localize(None).to_period("D")

ser = pd.Series(idx)
ser.iloc[-2] = pd.NaT
if as_categorical:
    ser = ser.astype("category")

self._check_replace_with_method(ser)
