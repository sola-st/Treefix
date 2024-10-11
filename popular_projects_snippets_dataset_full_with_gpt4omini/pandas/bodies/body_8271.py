# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
# GH 13149, GH 13209
idx = DatetimeIndex(["2016-05-16", "NaT", NaT, np.NaN], name="idx")

result = idx.astype("datetime64[ns]")
tm.assert_index_equal(result, idx)
assert result is not idx

result = idx.astype("datetime64[ns]", copy=False)
tm.assert_index_equal(result, idx)
assert result is idx

idx_tz = DatetimeIndex(["2016-05-16", "NaT", NaT, np.NaN], tz="EST", name="idx")
msg = "Cannot use .astype to convert from timezone-aware"
with pytest.raises(TypeError, match=msg):
    # dt64tz->dt64 deprecated
    result = idx_tz.astype("datetime64[ns]")
