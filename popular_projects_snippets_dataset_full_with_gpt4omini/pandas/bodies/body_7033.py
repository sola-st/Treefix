# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
klass = listlike_box

i = CategoricalIndex(list("aabbca"), categories=list("cab"), ordered=False)
cond = [True] * len(i)
expected = i
result = i.where(klass(cond))
tm.assert_index_equal(result, expected)

cond = [False] + [True] * (len(i) - 1)
expected = CategoricalIndex([np.nan] + i[1:].tolist(), categories=i.categories)
result = i.where(klass(cond))
tm.assert_index_equal(result, expected)
