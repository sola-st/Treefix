# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 6149
# coerce similarly for setitem and loc when rows have a null-slice
expected = DataFrame(
    {
        "date": Series(1.0, index=range(5)),
        "val": Series(range(5), dtype=np.int64),
    }
)
df = frame_for_consistency.copy()
df.loc[:, "date"] = 1.0
tm.assert_frame_equal(df, expected)
