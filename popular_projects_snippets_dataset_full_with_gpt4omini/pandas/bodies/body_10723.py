# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# describe
expected_index = Index([1, 3], name="A")
expected_col = MultiIndex(
    levels=[["B"], ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]],
    codes=[[0] * 8, list(range(8))],
)
expected = DataFrame(
    [
        [1.0, 2.0, np.nan, 2.0, 2.0, 2.0, 2.0, 2.0],
        [0.0, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    ],
    index=expected_index,
    columns=expected_col,
)
result = gb.describe()
tm.assert_frame_equal(result, expected)

expected = expected.reset_index()
result = gni.describe()
tm.assert_frame_equal(result, expected)
