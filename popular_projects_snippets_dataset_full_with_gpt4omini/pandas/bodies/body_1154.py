# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
df = DataFrame(
    {
        "jim": [0, 0, 1, 1],
        "joe": ["x", "x", "z", "y"],
        "jolie": np.random.rand(4),
    }
).set_index(["jim", "joe"])

with tm.assert_produces_warning(PerformanceWarning):
    df.loc[(1, "z")]

df = df.iloc[[2, 1, 3, 0]]
with tm.assert_produces_warning(PerformanceWarning):
    df.loc[(0,)]
