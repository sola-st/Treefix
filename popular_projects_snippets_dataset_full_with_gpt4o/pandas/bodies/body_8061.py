# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = getattr(tm, attr)(10)
expected = Index([1] * 10)
result = index.map(lambda x: 1)
tm.assert_index_equal(expected, result)
