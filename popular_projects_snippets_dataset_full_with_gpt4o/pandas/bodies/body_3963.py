# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 9406
df_nan = DataFrame(
    np.arange(4).reshape(2, 2),
    columns=MultiIndex.from_tuples(
        [("A", np.nan), ("B", "b")], names=["Upper", "Lower"]
    ),
    index=Index([0, 1], name="Num"),
    dtype=np.float64,
)
result = df_nan.stack()
expected = DataFrame(
    [[0.0, np.nan], [np.nan, 1], [2.0, np.nan], [np.nan, 3.0]],
    columns=Index(["A", "B"], name="Upper"),
    index=MultiIndex.from_tuples(
        [(0, np.nan), (0, "b"), (1, np.nan), (1, "b")], names=["Num", "Lower"]
    ),
)
tm.assert_frame_equal(result, expected)
