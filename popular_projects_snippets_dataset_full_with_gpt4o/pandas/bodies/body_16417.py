# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# GH 26045
result = cut(x, bins)
tm.assert_index_equal(result.categories, expected)
