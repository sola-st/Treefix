# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 3588
nan = np.nan
df = DataFrame(
    {
        "a": ["R1", "R2", nan, "R4"],
        "b": ["C1", "C2", "C3", "C4"],
        "c": [10, 15, 17, 20],
    }
)
if method:
    result = df.pivot(index="a", columns="b", values="c")
else:
    result = pd.pivot(df, index="a", columns="b", values="c")
expected = DataFrame(
    [
        [nan, nan, 17, nan],
        [10, nan, nan, nan],
        [nan, 15, nan, nan],
        [nan, nan, nan, 20],
    ],
    index=Index([nan, "R1", "R2", "R4"], name="a"),
    columns=Index(["C1", "C2", "C3", "C4"], name="b"),
)
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(df.pivot(index="b", columns="a", values="c"), expected.T)
