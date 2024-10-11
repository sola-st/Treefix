# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#24570
tx = pd.timedelta_range("09:30:00", "16:00:00", freq="30 min")
idx = MultiIndex.from_arrays([tx, np.arange(len(tx))])
assert tx[0] in idx
assert "element_not_exit" not in idx
assert "0 day 09:30:00" in idx
