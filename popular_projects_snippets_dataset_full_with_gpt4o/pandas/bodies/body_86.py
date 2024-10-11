# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series([1.5, np.nan, 3, np.nan, 5])

result = s.map(lambda x: x * 2, na_action="ignore")
exp = s * 2
tm.assert_series_equal(result, exp)
