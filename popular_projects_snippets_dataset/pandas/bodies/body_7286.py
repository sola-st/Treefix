# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
# GH 13149, GH 13209
idx = TimedeltaIndex([1e14, "NaT", NaT, np.NaN])

msg = (
    r"Cannot convert from timedelta64\[ns\] to timedelta64. "
    "Supported resolutions are 's', 'ms', 'us', 'ns'"
)
with pytest.raises(ValueError, match=msg):
    idx.astype("timedelta64")

result = idx.astype("timedelta64[ns]")
tm.assert_index_equal(result, idx)
assert result is not idx

result = idx.astype("timedelta64[ns]", copy=False)
tm.assert_index_equal(result, idx)
assert result is idx
