# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py
ser = series_with_interval_index.copy()

# this is a departure from our current
# indexing scheme, but simpler
with pytest.raises(KeyError, match=r"\[-1\] not in index"):
    indexer_sl(ser)[[-1, 3, 4, 5]]

with pytest.raises(KeyError, match=r"\[-1\] not in index"):
    indexer_sl(ser)[[-1, 3]]
