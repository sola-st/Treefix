# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 26996
values = [1, 2, 3, np.nan, 4, 5, 6]
expected_counts = [1.0, 2.0, 3.0, 2.0, 2.0, 2.0, 3.0]

# GH 31302
result = frame_or_series(values).rolling(3, min_periods=0).count()
expected = frame_or_series(expected_counts)
tm.assert_equal(result, expected)
