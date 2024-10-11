# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
dtype = IntervalDtype(subtype, index.closed)
result = index.astype(dtype)
expected = IntervalIndex.from_arrays(
    index.left.astype(subtype), index.right.astype(subtype), closed=index.closed
)
tm.assert_index_equal(result, expected)
