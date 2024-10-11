# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
result = index.dropna(how=how)
tm.assert_index_equal(result, expected)
