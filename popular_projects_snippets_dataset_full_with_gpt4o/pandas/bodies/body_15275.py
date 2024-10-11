# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
seq = datetime_series[[5, 10, 15]]
seq[1] = np.NaN
assert not np.isnan(datetime_series[10])
