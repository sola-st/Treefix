# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
cidx = CategoricalIndex(list("abc"))
result = cidx.get_loc("b")
assert result == 1
