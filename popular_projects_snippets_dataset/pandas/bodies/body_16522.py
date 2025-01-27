# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
# Check handling of empties
df = DataFrame(
    {
        "a": [1, 2, 2, 2, 2],
        "b": [3, 3, 4, 4, 4],
        "c": [np.nan, np.nan, np.nan, np.nan, np.nan],
    }
)

empty = DataFrame(
    [[0.0, 0.0], [0.0, 0.0]],
    index=Index([1, 2], name="a", dtype="int64"),
    columns=Index([3, 4], name="b"),
)

for i in [True, "index", "columns"]:
    calculated = crosstab(df.a, df.b, values=df.c, aggfunc="count", normalize=i)
    tm.assert_frame_equal(empty, calculated)

nans = DataFrame(
    [[0.0, np.nan], [0.0, 0.0]],
    index=Index([1, 2], name="a", dtype="int64"),
    columns=Index([3, 4], name="b"),
)
if using_array_manager:
    # INFO(ArrayManager) column without NaNs can preserve int dtype
    nans[3] = nans[3].astype("int64")

calculated = crosstab(df.a, df.b, values=df.c, aggfunc="count", normalize=False)
tm.assert_frame_equal(nans, calculated)
