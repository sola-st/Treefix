# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH 9336
expected = DataFrame(
    {
        "a": [0, 0, 0, 0, 13, 14],
        "b": [
            datetime(2012, 1, 1),
            1,
            "x",
            "y",
            datetime(2013, 1, 1),
            datetime(2014, 1, 1),
        ],
    }
)
df = DataFrame(0, columns=list("ab"), index=range(6))
df["b"] = pd.NaT
df.loc[0, "b"] = datetime(2012, 1, 1)
df.loc[1, "b"] = 1
df.loc[[2, 3], "b"] = "x", "y"
A = np.array(
    [
        [13, np.datetime64("2013-01-01T00:00:00")],
        [14, np.datetime64("2014-01-01T00:00:00")],
    ]
)
df.loc[[4, 5], ["a", "b"]] = A
tm.assert_frame_equal(df, expected)
