# Extracted from ./data/repos/pandas/pandas/tests/strings/test_get_dummies.py
# GH 12180
# Dummies named 'name' should work as expected
idx = Index(["a|b", "name|c", "b|name"])
result = idx.str.get_dummies("|")

expected = MultiIndex.from_tuples(
    [(1, 1, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1)], names=("a", "b", "c", "name")
)
tm.assert_index_equal(result, expected)
