# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
ser = Series([1, 2, 3])
result = Index(ser.array)
expected = Index([1, 2, 3])
tm.assert_index_equal(result, expected)
