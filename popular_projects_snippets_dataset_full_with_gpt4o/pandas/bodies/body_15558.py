# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# fail
ts = datetime_series[5:]
bool_ts = Series(np.zeros(len(ts), dtype=bool), index=ts.index)
filled_bool = bool_ts.reindex(datetime_series.index, method="pad")
assert isna(filled_bool[:5]).all()
