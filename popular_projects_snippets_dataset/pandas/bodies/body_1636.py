# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
d1, d2 = datetime_series.index[[5, 15]]

ts2 = datetime_series[::2][[1, 2, 0]]

msg = r"Timestamp\('2000-01-10 00:00:00'\)"
with pytest.raises(KeyError, match=msg):
    ts2.loc[d1:d2]
with pytest.raises(KeyError, match=msg):
    ts2.loc[d1:d2] = 0
