# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_base.py
klass = listlike_box

idx = simple_index
cond = [True] * len(idx)
expected = idx
result = expected.where(klass(cond))
tm.assert_index_equal(result, expected)

cond = [False] + [True] * len(idx[1:])
expected = IntervalIndex([np.nan] + idx[1:].tolist())
result = idx.where(klass(cond))
tm.assert_index_equal(result, expected)
