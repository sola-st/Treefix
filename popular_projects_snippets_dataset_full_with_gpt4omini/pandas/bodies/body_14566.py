# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = date_range("1/1/1987", freq="A", periods=3)
df = DataFrame({"A": ["x", "y", "z"], "B": [1, 2, 3]}, idx)

fig, ax = self.plt.subplots()
df.plot(ax=ax)  # it works
assert len(ax.get_lines()) == 1  # B was plotted
self.plt.close(fig)

msg = "no numeric data to plot"
with pytest.raises(TypeError, match=msg):
    df["A"].plot()
