# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot_multilevel.py
# GH 36360

df = pd.DataFrame(
    data=np.arange(12).reshape(4, 3),
    columns=MultiIndex.from_tuples(
        [(0, 0), (0, 1), (0, 2)], names=["col_L0", "col_L1"]
    ),
    index=MultiIndex.from_tuples(
        [(0, 0, 0), (0, 0, 1), (1, 1, 1), (1, 0, 0)],
        names=["idx_L0", "idx_L1", "idx_L2"],
    ),
)

res = df.pivot_table(
    index=["idx_L0"],
    columns=["idx_L1"],
    values=[(0, 1)],
    aggfunc=lambda col: col.values.sum(),
)

expected = pd.DataFrame(
    data=[[5, np.nan], [10, 7.0]],
    columns=MultiIndex.from_tuples(
        [(0, 1, 0), (0, 1, 1)], names=["col_L0", "col_L1", "idx_L1"]
    ),
    index=Index([0, 1], dtype="int64", name="idx_L0"),
)
if not using_array_manager:
    # BlockManager does not preserve the dtypes
    expected = expected.astype("float64")

tm.assert_frame_equal(res, expected)
