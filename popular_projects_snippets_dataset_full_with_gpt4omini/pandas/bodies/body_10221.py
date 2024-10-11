# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
# GH 21157
columns = MultiIndex.from_arrays([["M", "N"], ["P", "Q"]], names=["a", "b"])
df = DataFrame(np.ones((5, 2)), columns=columns)
result = df.rolling(3).corr()
expected = DataFrame(
    np.nan,
    index=MultiIndex.from_arrays(
        [
            np.repeat(np.arange(5, dtype=np.int64), 2),
            ["M", "N"] * 5,
            ["P", "Q"] * 5,
        ],
        names=[None, "a", "b"],
    ),
    columns=columns,
)
tm.assert_frame_equal(result, expected)
