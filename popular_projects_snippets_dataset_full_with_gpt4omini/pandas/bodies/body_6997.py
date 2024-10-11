# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# hits Index._concat
fst = Index(["a", "b"])
snd = CategoricalIndex(["d", "e"])
result = fst.append(snd)
expected = Index(["a", "b", "d", "e"])
tm.assert_index_equal(result, expected)
