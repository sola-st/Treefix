# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
# GH: 26476
obj = frame_or_series([0, 1, 2])
result = obj.expanding().sem()
if isinstance(result, DataFrame):
    result = Series(result[0].values)
expected = Series([np.nan] + [0.707107] * 2)
tm.assert_series_equal(result, expected)
