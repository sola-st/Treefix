# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# GH10698
named_series = Series([1, 2], name="foo")
unnamed_series1 = Series([1, 2])
unnamed_series2 = Series([4, 5])

result = concat([named_series, unnamed_series1, unnamed_series2], axis=1)
expected = DataFrame(
    {"foo": [1, 2], 0: [1, 2], 1: [4, 5]}, columns=["foo", 0, 1]
)
tm.assert_frame_equal(result, expected)

result = concat(
    [named_series, unnamed_series1, unnamed_series2],
    axis=1,
    keys=["red", "blue", "yellow"],
)
expected = DataFrame(
    {"red": [1, 2], "blue": [1, 2], "yellow": [4, 5]},
    columns=["red", "blue", "yellow"],
)
tm.assert_frame_equal(result, expected)

result = concat(
    [named_series, unnamed_series1, unnamed_series2], axis=1, ignore_index=True
)
expected = DataFrame({0: [1, 2], 1: [1, 2], 2: [4, 5]})
tm.assert_frame_equal(result, expected)
