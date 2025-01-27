# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_categorical.py
# GH 18050
ser = Series([(0, 0), (0, 1), (0, 0), (1, 0), (1, 1)])
expected = Series([True, False, True, False, False])
result = ser == (0, 0)
tm.assert_series_equal(result, expected)

result = ser.astype("category") == (0, 0)
tm.assert_series_equal(result, expected)
