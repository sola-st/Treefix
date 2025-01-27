# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
index = interval_range(0.0, 3.0, freq=0.25)
dtype = IntervalDtype(subtype, "right")
result = index.astype(dtype)
expected = IntervalIndex.from_arrays(
    index.left.astype(subtype), index.right.astype(subtype), closed=index.closed
)
tm.assert_index_equal(result, expected)
