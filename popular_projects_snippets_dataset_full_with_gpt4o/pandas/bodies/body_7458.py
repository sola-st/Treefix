# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH-24959
idx = MultiIndex.from_product([[1, pd.Timestamp("2000"), 2], ["a", "b"]])

other = MultiIndex.from_product([[3, pd.Timestamp("2000"), 4], ["c", "d"]])
# sort=None, the default
msg = "sort order is undefined for incomparable objects"
with tm.assert_produces_warning(RuntimeWarning, match=msg):
    result = idx.difference(other)
tm.assert_index_equal(result, idx)

# sort=False
result = idx.difference(other, sort=False)
tm.assert_index_equal(result, idx)
