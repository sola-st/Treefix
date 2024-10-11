# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 18789
index = IntervalIndex.from_breaks(breaks, closed=closed)
result = index.length
expected = Index(iv.length for iv in index)
tm.assert_index_equal(result, expected)

# with NA
index = index.insert(1, np.nan)
result = index.length
expected = Index(iv.length if notna(iv) else iv for iv in index)
tm.assert_index_equal(result, expected)
