# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
ts = datetime_series[::2]
int_ts = Series(np.zeros(len(ts), dtype=int), index=ts.index)

# this should work fine
reindexed_int = int_ts.reindex(datetime_series.index)

# if NaNs introduced
assert reindexed_int.dtype == np.float_

# NO NaNs introduced
reindexed_int = int_ts.reindex(int_ts.index[::2])
assert reindexed_int.dtype == np.int_
