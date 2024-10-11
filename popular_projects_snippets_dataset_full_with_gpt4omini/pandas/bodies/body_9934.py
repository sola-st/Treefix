# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH 26996
values = [1, 2, 3, np.nan, 4, 5, 6]
expected_counts = [1.0, 2.0, 3.0, 3.0, 4.0, 5.0, 6.0]

result = frame_or_series(values).expanding().count()
expected = frame_or_series(expected_counts)
tm.assert_equal(result, expected)
