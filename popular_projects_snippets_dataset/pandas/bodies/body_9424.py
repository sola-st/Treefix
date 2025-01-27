# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
# GH#33701

result = pd.NA * pd.Series(np.zeros(10001))
expected = pd.Series([pd.NA] * 10001)

tm.assert_series_equal(result, expected)
