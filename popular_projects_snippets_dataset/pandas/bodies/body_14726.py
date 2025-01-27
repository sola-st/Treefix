# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
df = DataFrame(np.random.rand(3, 3), columns=["a", "b", "c"])
ax = df.plot(kind=kind, legend=False)
self._check_legend_labels(ax, visible=False)
