# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# test if xlim is set correctly when ax contains multiple different kinds
# of plots, GH 27686
fig, ax = self.plt.subplots()

indexes = ["k1", "k2", "k3", "k4"]
df = DataFrame(
    {
        "s1": [1000, 2000, 1500, 2000],
        "s2": [900, 1400, 2000, 3000],
        "s3": [1500, 1500, 1600, 1200],
        "secondary_y": [1, 3, 4, 3],
    },
    index=indexes,
)
df[["s1", "s2", "s3"]].plot.bar(ax=ax, stacked=False)
df[["secondary_y"]].plot(ax=ax, secondary_y=True)

xlims = ax.get_xlim()
assert xlims[0] < 0
assert xlims[1] > 3

# make sure axis labels are plotted correctly as well
xticklabels = [t.get_text() for t in ax.get_xticklabels()]
assert xticklabels == indexes
