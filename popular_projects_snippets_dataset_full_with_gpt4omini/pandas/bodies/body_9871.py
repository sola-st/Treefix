# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#40002
idx = date_range(start="2020-01-01", end="2020-01-03", freq="1d")
obj = frame_or_series(range(1, 4), index=idx)
result = obj.rolling("1d", closed="left").sum()
expected = frame_or_series([np.nan, 1, 2], index=idx)
tm.assert_equal(result, expected)

result = obj.iloc[::-1].rolling("1d", closed="left").sum()
idx = date_range(start="2020-01-03", end="2020-01-01", freq="-1d")
expected = frame_or_series([np.nan, 3, 2], index=idx)
tm.assert_equal(result, expected)
