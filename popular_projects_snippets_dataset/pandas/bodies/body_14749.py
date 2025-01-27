# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(5, 5))

# regular
ax = df.plot.bar(linewidth=2)
for r in ax.patches:
    assert r.get_linewidth() == 2

# stacked
ax = df.plot.bar(stacked=True, linewidth=2)
for r in ax.patches:
    assert r.get_linewidth() == 2

# subplots
axes = df.plot.bar(linewidth=2, subplots=True)
self._check_axes_shape(axes, axes_num=5, layout=(5, 1))
for ax in axes:
    for r in ax.patches:
        assert r.get_linewidth() == 2
