# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
df = DataFrame(
    {
        "A": np.random.uniform(size=20),
        "B": np.random.uniform(size=20),
        "C": np.arange(20) + np.random.uniform(size=20),
    }
)
ax = df.plot.hexbin(x="A", y="B", colorbar=None)
assert ax.collections[0].colorbar is None
