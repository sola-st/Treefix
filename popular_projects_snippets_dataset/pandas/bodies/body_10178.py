# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
df = DataFrame([1, 2, 3, 4, 5, 6, 7, 8])
result = (
    df.groupby([1, 2, 1, 2, 1, 2, 1, 2])
    .rolling(window=window, min_periods=min_periods, closed=closed)
    .var(0)
)
expected_result = DataFrame(
    np.array(expected, dtype="float64"),
    index=MultiIndex(
        levels=[np.array([1, 2]), [0, 1, 2, 3, 4, 5, 6, 7]],
        codes=[[0, 0, 0, 0, 1, 1, 1, 1], [0, 2, 4, 6, 1, 3, 5, 7]],
    ),
)
tm.assert_frame_equal(result, expected_result)
