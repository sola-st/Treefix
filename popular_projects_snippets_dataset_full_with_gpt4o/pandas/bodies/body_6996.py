# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_append.py
# GH#14298 - if base object is not categorical -> coerce to object
result = Index(["c", "a"]).append(ci)
expected = Index(list("caaabbca"))
tm.assert_index_equal(result, expected, exact=True)
