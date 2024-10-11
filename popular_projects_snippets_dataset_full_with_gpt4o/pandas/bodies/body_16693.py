# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# timedelta64 issues with join/merge
# GH 5695
td = np.timedelta64(300000000)
lhs = DataFrame(Series([td, td], index=["A", "B"]))
rhs = DataFrame(Series([td], index=["A"]))

result = lhs.join(rhs, rsuffix="r", how="left")
expected = DataFrame(
    {
        "0": Series([td, td], index=list("AB")),
        "0r": Series([td, pd.NaT], index=list("AB")),
    }
)
tm.assert_frame_equal(result, expected)
