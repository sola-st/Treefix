# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# A series other than float, int, string, or object
ts = datetime_series[::2]
bool_ts = Series(np.zeros(len(ts), dtype=bool), index=ts.index)

# this should work fine
reindexed_bool = bool_ts.reindex(datetime_series.index)

# if NaNs introduced
assert reindexed_bool.dtype == np.object_

# NO NaNs introduced
reindexed_bool = bool_ts.reindex(bool_ts.index[::2])
assert reindexed_bool.dtype == np.bool_
