# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame(
    {
        "a": np.random.randn(100),
        "b": np.random.randn(100),
        "group": np.random.choice(["group1", "group2"], 100),
    }
)
xlabel, ylabel = "x", "y"
ax = df.plot(kind="box", vert=vert, xlabel=xlabel, ylabel=ylabel)
assert ax.get_xlabel() == xlabel
assert ax.get_ylabel() == ylabel
