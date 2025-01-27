# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 8844
full_multiindex = MultiIndex.from_tuples(
    [("B", "x"), ("B", "z"), ("A", "y"), ("C", "x"), ("C", "u")],
    names=["Upper", "Lower"],
)
df = DataFrame(np.arange(6).reshape(2, 3), columns=full_multiindex[[0, 1, 3]])
result = df.stack(dropna=False)
expected = DataFrame(
    [[0, 2], [1, np.nan], [3, 5], [4, np.nan]],
    index=MultiIndex(
        levels=[[0, 1], ["u", "x", "y", "z"]],
        codes=[[0, 0, 1, 1], [1, 3, 1, 3]],
        names=[None, "Lower"],
    ),
    columns=Index(["B", "C"], name="Upper"),
)
expected["B"] = expected["B"].astype(df.dtypes[0])
tm.assert_frame_equal(result, expected)
