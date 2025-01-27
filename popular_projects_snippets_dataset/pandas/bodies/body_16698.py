# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
left = DataFrame(
    {
        "key": [1, 2],
        "value": pd.date_range("20151010", periods=2, tz="US/Eastern"),
    }
)
right = DataFrame(
    {
        "key": [2, 3],
        "value": pd.date_range("20151011", periods=2, tz="US/Eastern"),
    }
)
expected = DataFrame(
    {
        "key": [1, 2, 3],
        "value_x": list(pd.date_range("20151010", periods=2, tz="US/Eastern"))
        + [pd.NaT],
        "value_y": [pd.NaT]
        + list(pd.date_range("20151011", periods=2, tz="US/Eastern")),
    }
)
result = merge(left, right, on="key", how="outer")
tm.assert_frame_equal(result, expected)
assert result["value_x"].dtype == "datetime64[ns, US/Eastern]"
assert result["value_y"].dtype == "datetime64[ns, US/Eastern]"
