# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
index = MultiIndex.from_tuples([("A", 0), ("A", 1), ("B", 1)], names=["a", "b"])
df = DataFrame(
    {
        "A": pd.array([0, 1, None], dtype="Int64"),
        "B": pd.Categorical(["a", "a", "b"]),
    },
    index=index,
)

result = df.unstack(level=level)
expected = df.astype(object).unstack(level=level)

expected_dtypes = Series(
    [df.A.dtype] * 2 + [df.B.dtype] * 2, index=result.columns
)
tm.assert_series_equal(result.dtypes, expected_dtypes)
tm.assert_frame_equal(result.astype(object), expected)
