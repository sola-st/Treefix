# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame(
    {"key": [1, 2], "value": pd.period_range("20151010", periods=2, freq="D")}
)
right = DataFrame(
    {"key": [2, 3], "value": pd.period_range("20151011", periods=2, freq="D")}
)

exp_x = pd.period_range("20151010", periods=2, freq="D")
exp_y = pd.period_range("20151011", periods=2, freq="D")
expected = DataFrame(
    {
        "key": [1, 2, 3],
        "value_x": list(exp_x) + [pd.NaT],
        "value_y": [pd.NaT] + list(exp_y),
    }
)
result = merge(left, right, on="key", how="outer")
tm.assert_frame_equal(result, expected)
assert result["value_x"].dtype == "Period[D]"
assert result["value_y"].dtype == "Period[D]"
