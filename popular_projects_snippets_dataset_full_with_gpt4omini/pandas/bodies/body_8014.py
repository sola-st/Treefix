# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
dti = date_range("2016-01-01", periods=3)
result = Index(dti, dtype="Period[D]")
expected = dti.to_period("D")
tm.assert_index_equal(result, expected)
