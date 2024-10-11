# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
cidx = CategoricalIndex(list("abbc"))
result = cidx.get_loc("b")
expected = slice(1, 3, None)
assert result == expected
