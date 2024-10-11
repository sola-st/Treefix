# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_astype.py
ci = CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)

result = ci.astype(object)
tm.assert_index_equal(result, Index(np.array(ci)))

# this IS equal, but not the same class
assert result.equals(ci)
assert isinstance(result, Index)
assert not isinstance(result, CategoricalIndex)

# interval
ii = IntervalIndex.from_arrays(left=[-0.001, 2.0], right=[2, 4], closed="right")

ci = CategoricalIndex(
    Categorical.from_codes([0, 1, -1], categories=ii, ordered=True)
)

result = ci.astype("interval")
expected = ii.take([0, 1, -1], allow_fill=True, fill_value=np.nan)
tm.assert_index_equal(result, expected)

result = IntervalIndex(result.values)
tm.assert_index_equal(result, expected)
