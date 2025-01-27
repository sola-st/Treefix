# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
index = Index(["a", "b", "c", "d"], name="index")
result = index.delete(pos)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
