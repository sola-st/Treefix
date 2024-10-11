# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#43209
df = DataFrame(
    [[1, 2, 3, 4, 5, 6]] * 3,
    columns=MultiIndex.from_product([["a", "b"], ["i", "j", "k"]]),
).astype({("a", "j"): dtype, ("b", "j"): dtype})
result = df.groupby(level=1, axis=1).agg(func)
expected = DataFrame([expected] * 3, columns=["i", "j", "k"]).astype(
    result_dtype_dict
)
tm.assert_frame_equal(result, expected)
