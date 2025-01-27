# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# pre-2.0 we required exact tz match, in 2.0 we require only
#  tzawareness-match
data = np.array([1, 2, 3], dtype="M8[ns]")
arr = DatetimeArray(data, copy=False, dtype=DatetimeTZDtype(tz="US/Central"))
with pytest.raises(TypeError, match="Cannot compare tz-naive and tz-aware"):
    arr[0] = pd.Timestamp("2000")

ts = pd.Timestamp("2000", tz="US/Eastern")
arr[0] = ts
assert arr[0] == ts.tz_convert("US/Central")
