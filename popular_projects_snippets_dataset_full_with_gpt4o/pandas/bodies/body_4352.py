# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
# GH#38367
intervals = [Interval(1, 2), Interval(3, 4)]
data = DataFrame(
    [[1, np.nan], [2, np.nan]],
    columns=CategoricalIndex(
        intervals, categories=intervals + [Interval(5, 6)]
    ),
)
mask = DataFrame(
    [[False, False], [False, False]], columns=data.columns, dtype=bool
)
result = mask | isnull(data)
expected = DataFrame(
    [[False, True], [False, True]],
    columns=CategoricalIndex(
        intervals, categories=intervals + [Interval(5, 6)]
    ),
)
tm.assert_frame_equal(result, expected)
