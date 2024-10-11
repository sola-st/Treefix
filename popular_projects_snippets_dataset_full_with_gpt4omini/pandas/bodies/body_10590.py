# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH 21240
df = DataFrame({"a": [1], "b": [2], "c": [True]})
df["c"] = df["c"].astype(input_dtype)
op = getattr(df.groupby(keys)[["c"]], method)
result = op(lambda x: x.astype(result_dtype).iloc[0])
expected_index = pd.RangeIndex(0, 1) if method == "transform" else agg_index
expected = DataFrame({"c": [df["c"].iloc[0]]}, index=expected_index).astype(
    result_dtype
)
if method == "apply":
    expected.columns.names = [0]
tm.assert_frame_equal(result, expected)
