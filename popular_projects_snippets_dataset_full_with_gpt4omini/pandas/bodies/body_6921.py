# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
# GH#22295
# test there is no mangling of NA values
expected = Index(["a", nulls_fixture, "b", "c"])
result = Index(list("abc")).insert(1, nulls_fixture)
tm.assert_index_equal(result, expected)
