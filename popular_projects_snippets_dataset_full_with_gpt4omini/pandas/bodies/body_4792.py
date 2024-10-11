# Extracted from ./data/repos/pandas/pandas/tests/strings/test_get_dummies.py
# GH9980, GH8028
idx = Index(["a|b", "a|c", "b|c"])
result = idx.str.get_dummies("|")

expected = MultiIndex.from_tuples(
    [(1, 1, 0), (1, 0, 1), (0, 1, 1)], names=("a", "b", "c")
)
tm.assert_index_equal(result, expected)
