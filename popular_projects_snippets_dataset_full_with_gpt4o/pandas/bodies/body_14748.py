# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH37942
df = DataFrame(np.random.rand(4, 2), columns=["x", "y"])
fig, (ax1, ax2) = self.plt.subplots(1, 2, sharey=True)

df.plot(ax=ax1, kind="area")
df.plot(ax=ax2, kind="area")

assert self.get_y_axis(ax1).joined(ax1, ax2)
assert self.get_y_axis(ax2).joined(ax1, ax2)
