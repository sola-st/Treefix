# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
result = series.expanding(min_periods=0).count()
tm.assert_almost_equal(
    result, series.rolling(window=len(series), min_periods=0).count()
)
