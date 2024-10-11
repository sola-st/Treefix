# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
repeats = 2
index = Index([1, 2, 3])
expected = Index([1, 1, 2, 2, 3, 3])

result = index.repeat(repeats)
tm.assert_index_equal(result, expected)
