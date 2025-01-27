# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 11704
ser = Series(range(5), index=date_range(start="2020-01-01", periods=5, freq="D"))

expected = [
    Series(values, index=idx) for (values, idx) in zip(expected, expected_index)
]

for (expected, actual) in zip(expected, ser.rolling(window)):
    tm.assert_series_equal(actual, expected)
