# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
B = np.concatenate((np.arange(10000), np.arange(10000), np.arange(5000)))
A = np.arange(25000)
df = DataFrame({"A": A, "B": B, "C": A, "D": B, "E": np.random.randn(25000)})

left = df.groupby(["A", "B", "C", "D"]).sum()
right = df.groupby(["D", "C", "B", "A"]).sum()
assert len(left) == len(right)
