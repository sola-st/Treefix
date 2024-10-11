# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH#11818
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
msg = r"Cannot convert arg \[datetime\.datetime\(2010, 1, 2, 1, 0\)\] to a time"
with pytest.raises(ValueError, match=msg):
    rng.indexer_between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))
