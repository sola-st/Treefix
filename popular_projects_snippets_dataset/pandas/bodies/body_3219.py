# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_explode.py
df = pd.DataFrame(
    {scalar: pd.Series([[0, 1, 2], np.nan, [], (3, 4)], index=list("abcd")), "B": 1}
)
result = df.explode(scalar)
expected = pd.DataFrame(
    {
        scalar: pd.Series(
            [0, 1, 2, np.nan, np.nan, 3, 4], index=list("aaabcdd"), dtype=object
        ),
        "B": 1,
    }
)
tm.assert_frame_equal(result, expected)
