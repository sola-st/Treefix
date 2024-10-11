# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_astype.py
arr = period_array(["2000", "2001", None], freq="D")
result = arr.astype(PeriodDtype("M"))
expected = period_array(["2000", "2001", None], freq="M")
tm.assert_period_array_equal(result, expected)
