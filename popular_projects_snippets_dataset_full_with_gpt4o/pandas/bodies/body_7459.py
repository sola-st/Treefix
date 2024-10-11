# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
idx = MultiIndex.from_product([[1, pd.Timestamp("2000"), 2], ["a", "b"]])
other = MultiIndex.from_product([[3, pd.Timestamp("2000"), 4], ["c", "d"]])

msg = "The 'sort' keyword only takes the values of None or False; True was passed."
with pytest.raises(ValueError, match=msg):
    idx.difference(other, sort=True)
