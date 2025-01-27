# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# Example from GH33819
# Create data
df = DataFrame({"a": np.random.randn(1000), "b": np.random.randn(1000)})

# Create figure
fig = self.plt.figure()
plots = fig.subplots(2, 3)

# Create *externally* shared axes
plots[0][0] = fig.add_subplot(231, sharex=plots[1][0])
# note: no plots[0][1] that's the twin only case
plots[0][2] = fig.add_subplot(233, sharex=plots[1][2])

# Create *internally* shared axes
# note: no plots[0][0] that's the external only case
twin_ax1 = plots[0][1].twinx()
twin_ax2 = plots[0][2].twinx()

# Plot data to primary axes
df["a"].plot(ax=plots[0][0], title="External share only").set_xlabel(
    "this label should never be visible"
)
df["a"].plot(ax=plots[1][0])

df["a"].plot(ax=plots[0][1], title="Internal share (twin) only").set_xlabel(
    "this label should always be visible"
)
df["a"].plot(ax=plots[1][1])

df["a"].plot(ax=plots[0][2], title="Both").set_xlabel(
    "this label should never be visible"
)
df["a"].plot(ax=plots[1][2])

# Plot data to twinned axes
df["b"].plot(ax=twin_ax1, color="green")
df["b"].plot(ax=twin_ax2, color="yellow")

assert not plots[0][0].xaxis.get_label().get_visible()
assert plots[0][1].xaxis.get_label().get_visible()
assert not plots[0][2].xaxis.get_label().get_visible()
