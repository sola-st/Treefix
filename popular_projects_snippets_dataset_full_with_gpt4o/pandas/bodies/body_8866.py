# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = DatetimeArray(data, freq="D")
if index:
    arr = pd.Index(arr)

mismatch = arr.tz_localize("Asia/Tokyo")

msg = "Cannot compare tz-naive and tz-aware datetime-like objects"
with pytest.raises(TypeError, match=msg):
    arr.searchsorted(mismatch[0])
with pytest.raises(TypeError, match=msg):
    arr.searchsorted(mismatch)

with pytest.raises(TypeError, match=msg):
    mismatch.searchsorted(arr[0])
with pytest.raises(TypeError, match=msg):
    mismatch.searchsorted(arr)
