# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
result = MultiIndex.from_product([[]], names=["A"])
expected = Index([], name="A")
tm.assert_index_equal(result.levels[0], expected)
assert result.names == ["A"]
