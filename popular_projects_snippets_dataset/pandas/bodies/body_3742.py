# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
df = DataFrame(
    {
        "A": np.random.randn(5),
        "B": np.random.randn(5),
        "C": np.random.randn(5),
        "D": ["a", "b", "c", "d", "e"],
    }
)
df.iloc[2, [0, 1, 2]] = np.nan
df.iloc[0, 0] = np.nan
df.iloc[1, 1] = np.nan
df.iloc[:, 3] = np.nan
expected = df.dropna(subset=["A", "B", "C"], how="all")
expected.columns = ["A", "A", "B", "C"]

df.columns = ["A", "A", "B", "C"]

result = df.dropna(subset=["A", "C"], how="all")
tm.assert_frame_equal(result, expected)
