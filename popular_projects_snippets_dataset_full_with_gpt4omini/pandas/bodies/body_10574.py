# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#43209
df = DataFrame(
    np.arange(12).reshape(3, 4),
    index=Index([0, 1, 0], name="y"),
    columns=Index([10, 20, 10, 20], name="x"),
    dtype="int64",
).astype({10: "Int64"})
result = df.groupby("x", axis=1).agg(func)
expected = DataFrame(
    data=expected_data,
    index=Index([0, 1, 0], name="y"),
    columns=Index([10, 20], name="x"),
).astype(result_dtype_dict)
tm.assert_frame_equal(result, expected)
