# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 26011
df = DataFrame(
    {
        "a": [np.nan, "a", np.nan, "b", np.nan],
        "b": [0, 2, 4, 6, 8],
        "c": [1, 3, 5, 7, 9],
    }
)
result = df.groupby("a").nth(0, dropna=dropna)
expected = df.iloc[[1, 3]]

tm.assert_frame_equal(result, expected)
