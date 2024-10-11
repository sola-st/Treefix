# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
result = _get_combined_index([])
expected = Index([])
tm.assert_index_equal(result, expected)
