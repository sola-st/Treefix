# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
idx = DatetimeIndex(["2000-01-03", "2000-01-01", "2000-01-02"])
ordered = DatetimeIndex(idx.sort_values(), freq="infer")
result = ordered.union(idx, sort=sort)
tm.assert_index_equal(result, ordered)

result = ordered[:0].union(ordered, sort=sort)
tm.assert_index_equal(result, ordered)
assert result.freq == ordered.freq
