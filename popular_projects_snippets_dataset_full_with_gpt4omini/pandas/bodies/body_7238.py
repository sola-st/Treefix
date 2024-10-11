# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
cond = [True] * len(index)
expected = index
result = index.where(listlike_box(cond))

cond = [False] + [True] * (len(index) - 1)
expected = Index([index._na_value] + index[1:].tolist(), dtype=np.float64)
result = index.where(listlike_box(cond))
tm.assert_index_equal(result, expected)
