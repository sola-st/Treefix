# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    {
        "A": np.random.uniform(size=20),
        "B": np.random.uniform(size=20),
        "C": np.arange(20) + np.random.uniform(size=20),
    }
)

ax = df.plot.hexbin(x="A", y="B", C="C")
assert len(ax.collections) == 1

ax = df.plot.hexbin(x="A", y="B", C="C", reduce_C_function=np.std)
assert len(ax.collections) == 1
