# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame(
    {
        "a": np.random.randn(100),
        "b": np.random.randn(100),
        "group": np.random.choice(["group1", "group2"], 100),
    }
)
xlabel, ylabel = "x", "y"
ax = df.boxplot(by="group", vert=vert, xlabel=xlabel, ylabel=ylabel)
for subplot in ax:
    assert subplot.get_xlabel() == xlabel
    assert subplot.get_ylabel() == ylabel
self.plt.close()

ax = df.boxplot(by="group", vert=vert)
for subplot in ax:
    target_label = subplot.get_xlabel() if vert else subplot.get_ylabel()
    assert target_label == pprint_thing(["group"])
self.plt.close()
