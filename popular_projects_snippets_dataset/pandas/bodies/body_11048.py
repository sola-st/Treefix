# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 21651
expected = DataFrame(
    {
        "date": pd.date_range("2010-01-01", freq="12H", periods=5),
        "vals": range(5),
        "let": list("abcde"),
    }
)
result = expected.groupby(
    [expected.let, expected.date.dt.date], group_keys=False
).apply(lambda x: x.iloc[0:])
tm.assert_frame_equal(result, expected)
