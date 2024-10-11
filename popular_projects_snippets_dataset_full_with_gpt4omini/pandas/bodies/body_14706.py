# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
np.random.seed(0)
df = DataFrame(np.random.randn(30, 2), columns=["A", "B"])
df["C"] = np.random.choice(["a", "b", "c"], 30)
df["D"] = np.random.choice(["a", "b", "c"], 30)
exit(df)
