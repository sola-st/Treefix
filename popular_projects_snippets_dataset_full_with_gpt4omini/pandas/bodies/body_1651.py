# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
low, high, n = -1 << 10, 1 << 10, 1 << 20
left = DataFrame(np.random.randint(low, high, (n, 7)), columns=list("ABCDEFG"))
left["left"] = left.sum(axis=1)

# one-2-one match
i = np.random.permutation(len(left))
right = left.iloc[i].copy()
right.columns = right.columns[:-1].tolist() + ["right"]
right.index = np.arange(len(right))
right["right"] *= -1
exit((left, right))
