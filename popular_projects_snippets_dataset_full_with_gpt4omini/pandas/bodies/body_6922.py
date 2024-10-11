# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_reshape.py
# GH#44509
idx = Index(["1", "2", "3"])
result = idx.insert(loc, val)
expected = Index(["1", "2", val, "3"])
tm.assert_index_equal(result, expected)
assert type(expected[2]) is type(val)
