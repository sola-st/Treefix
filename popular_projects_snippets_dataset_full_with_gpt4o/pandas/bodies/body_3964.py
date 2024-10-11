# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 14018
idx = MultiIndex.from_product([["A"], [0, 1]])
df = DataFrame({"cat": pd.Categorical(["a", "b"])}, index=idx)
result = df.unstack()
expected = DataFrame(
    {
        0: pd.Categorical(["a"], categories=["a", "b"]),
        1: pd.Categorical(["b"], categories=["a", "b"]),
    },
    index=["A"],
)
expected.columns = MultiIndex.from_tuples([("cat", 0), ("cat", 1)])
tm.assert_frame_equal(result, expected)
