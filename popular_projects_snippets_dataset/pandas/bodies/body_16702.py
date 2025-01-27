# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame(
    {"key": pd.period_range("20151010", periods=2, freq="D"), "value": [1, 2]}
)
right = DataFrame(
    {
        "key": pd.period_range("20151011", periods=3, freq="D"),
        "value": [1, 2, 3],
    }
)

expected = DataFrame(
    {
        "key": pd.period_range("20151010", periods=4, freq="D"),
        "value_x": [1, 2, np.nan, np.nan],
        "value_y": [np.nan, 1, 2, 3],
    }
)
result = merge(left, right, on="key", how="outer")
tm.assert_frame_equal(result, expected)
