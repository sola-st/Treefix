# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH36189
s = Series([4] * 3)
result = s.apply(["sum", lambda x: x.sum(), lambda x: x.sum()])
expected = Series([12, 12, 12], index=["sum", "<lambda>", "<lambda>"])

tm.assert_series_equal(result, expected)
