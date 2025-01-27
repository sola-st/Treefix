# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
rng = date_range("1/1/2000", "3/1/2000", freq="B")

# neither monotonic increasing or decreasing
rng2 = rng[[1, 0, 2]]

msg = "index must be monotonic increasing or decreasing"
with pytest.raises(ValueError, match=msg):
    rng2.get_indexer(rng, method="pad")
