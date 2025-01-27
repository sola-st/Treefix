# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_setops.py
index = period_range("1/1/2000", "1/20/2000", freq="D")

result = index[:-5].union(index[10:], sort=sort)
tm.assert_index_equal(result, index)

# not in order
result = _permute(index[:-5]).union(_permute(index[10:]), sort=sort)
if sort is None:
    tm.assert_index_equal(result, index)
assert tm.equalContents(result, index)

# cast if different frequencies
index = period_range("1/1/2000", "1/20/2000", freq="D")
index2 = period_range("1/1/2000", "1/20/2000", freq="W-WED")
result = index.union(index2, sort=sort)
expected = index.astype(object).union(index2.astype(object), sort=sort)
tm.assert_index_equal(result, expected)
