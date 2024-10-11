# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 11704
expected = [Series(values, index=index) for (values, index) in expected]

for (expected, actual) in zip(
    expected, ser.rolling(window, min_periods=min_periods)
):
    tm.assert_series_equal(actual, expected)
