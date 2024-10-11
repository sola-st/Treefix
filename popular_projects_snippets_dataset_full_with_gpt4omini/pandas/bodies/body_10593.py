# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#37493
df = DataFrame(
    {"a": [1, 1, 2, 3, 4, 4], "b": [22, 11, pd.NA, 10, 20, pd.NA]},
    dtype=any_numeric_ea_dtype,
)
result = df.groupby("a").ohlc()
expected = DataFrame(
    [[22, 22, 11, 11], [pd.NA] * 4, [10] * 4, [20] * 4],
    columns=MultiIndex.from_product([["b"], ["open", "high", "low", "close"]]),
    index=Index([1, 2, 3, 4], dtype=any_numeric_ea_dtype, name="a"),
    dtype=any_numeric_ea_dtype,
)
tm.assert_frame_equal(result, expected)
