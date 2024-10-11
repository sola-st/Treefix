# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# callable
idx = simple_index

result = idx.map(lambda x: x)
# RangeIndex are equivalent to the similar NumericIndex with int64 dtype
tm.assert_index_equal(result, idx, exact="equiv")
