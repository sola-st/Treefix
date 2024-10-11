# Extracted from ./data/repos/pandas/pandas/tests/resample/test_base.py
# GH13212
df = empty_frame_dti
# count retains dimensions too
result = getattr(df.resample(freq, group_keys=False), resample_method)()
if resample_method != "size":
    expected = df.copy()
else:
    # GH14962
    expected = Series([], dtype=np.int64)

expected.index = _asfreq_compat(df.index, freq)

tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
tm.assert_almost_equal(result, expected)
