# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH#21275
obj = frame_or_series(
    range(periods),
    index=date_range("2016-1-1 00:00:00", periods=periods, freq="H"),
)

result = obj.shift(1, "2H")

expected = frame_or_series(
    range(periods),
    index=date_range("2016-1-1 02:00:00", periods=periods, freq="H"),
)
tm.assert_equal(result, expected)
