# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 15819 Verifies that datetime and integer rolling windows can be
# applied to empty DataFrames
expected = DataFrame()
result = DataFrame().rolling(roller).sum()
tm.assert_frame_equal(result, expected)

# Verifies that datetime and integer rolling windows can be applied to
# empty DataFrames with datetime index
expected = DataFrame(index=DatetimeIndex([]))
result = DataFrame(index=DatetimeIndex([])).rolling(roller).sum()
tm.assert_frame_equal(result, expected)
