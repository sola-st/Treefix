# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
rep = 2
idx = simple_index.copy()
new_index_cls = (
    NumericIndex if isinstance(idx, RangeIndex) else idx._constructor
)
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
tm.assert_index_equal(idx.repeat(rep), expected)

idx = simple_index
rep = np.arange(len(idx))
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
tm.assert_index_equal(idx.repeat(rep), expected)
