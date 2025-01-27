# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_first_and_last.py
# GH#29623
x = frame_or_series([1] * 100, index=bdate_range("2010-03-31", periods=100))
result = x.first("2M")
expected = frame_or_series(
    [1] * 23, index=bdate_range("2010-03-31", "2010-04-30")
)
tm.assert_equal(result, expected)
