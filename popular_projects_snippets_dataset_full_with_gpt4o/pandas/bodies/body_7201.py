# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# https://github.com/pandas-dev/pandas/issues/35217
float_index = Index([1.0, 2, 3])
string_index = Index(["1", "2", "3"])

result = float_index.difference(string_index)
tm.assert_index_equal(result, float_index)

result = string_index.difference(float_index)
tm.assert_index_equal(result, string_index)
