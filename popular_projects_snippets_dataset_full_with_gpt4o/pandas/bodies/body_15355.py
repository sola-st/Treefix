# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# missing
d = datetime_series.index[0] - BDay()
msg = r"Timestamp\('1999-12-31 00:00:00'\)"
with pytest.raises(KeyError, match=msg):
    datetime_series[d]
