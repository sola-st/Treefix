# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_timedeltas.py
data = np.arange(10, dtype="i8") * 24 * 3600 * 10**9
arr = TimedeltaArray(data, freq="D")
if index:
    arr = pd.Index(arr)

msg = "|".join(
    [
        "searchsorted requires compatible dtype or scalar",
        "value should be a 'Timedelta', 'NaT', or array of those. Got",
    ]
)
with pytest.raises(TypeError, match=msg):
    arr.searchsorted(other)
