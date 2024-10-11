# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#18400
expected = NumericIndex([0, 1, 2, 3], dtype=dtype)
result = Index([0.0, 1.0, 2.0, 3.0], dtype=dtype)
tm.assert_index_equal(result, expected)
