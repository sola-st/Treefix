# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH#24903
result = (
    DataFrame(
        {
            "a": [1, 1, 2, 2],
            "b": ["", "", "", ""],
            "c": pd.to_datetime([1, 2, 3, 4], unit="s"),
        }
    )
    .groupby(["a", "b"])
    .apply(lambda df: df.iloc[-1])
)
expected = DataFrame(
    [[1, "", pd.to_datetime(2, unit="s")], [2, "", pd.to_datetime(4, unit="s")]],
    columns=["a", "b", "c"],
    index=MultiIndex.from_tuples([(1, ""), (2, "")], names=["a", "b"]),
)
tm.assert_frame_equal(result, expected)
