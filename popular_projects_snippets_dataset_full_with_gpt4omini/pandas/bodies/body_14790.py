# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    {
        "A": np.random.uniform(size=20),
        "B": np.random.uniform(size=20),
        "C": np.arange(20) + np.random.uniform(size=20),
    }
)
ax = df.plot.hexbin(x="A", y="B", **kwargs)
assert ax.collections[0].cmap.name == expected
