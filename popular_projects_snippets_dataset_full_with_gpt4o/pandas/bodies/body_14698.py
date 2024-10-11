# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 25261
idx = date_range(start="now", periods=10)
df = DataFrame(np.random.rand(10, 3), index=idx)
kwargs = {}
if hasattr(self.plt.Figure, "get_constrained_layout"):
    kwargs["constrained_layout"] = True
fig, axes = self.plt.subplots(2, **kwargs)
with tm.assert_produces_warning(None):
    df.plot(ax=axes[0])
    with tm.ensure_clean(return_filelike=True) as path:
        self.plt.savefig(path)
