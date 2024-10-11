# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_and_last.py
# GH#29623
x = frame_or_series([1] * 100, index=bdate_range(start, periods=100))
result = x.first("1M")
expected = frame_or_series(
    [1] * periods, index=bdate_range(start, periods=periods)
)
tm.assert_equal(result, expected)
