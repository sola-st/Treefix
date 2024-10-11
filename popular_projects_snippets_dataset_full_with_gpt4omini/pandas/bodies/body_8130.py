# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 6194
index = Index(vals, dtype=dtype)
result = index.dropna(how=how)
expected = Index(expected, dtype=dtype)
tm.assert_index_equal(result, expected)
