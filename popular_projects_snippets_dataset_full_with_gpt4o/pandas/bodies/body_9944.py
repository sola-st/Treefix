# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
result = series.expanding().quantile(0.5)

rolling_result = series.rolling(window=len(series), min_periods=1).quantile(0.5)

tm.assert_almost_equal(result, rolling_result)
