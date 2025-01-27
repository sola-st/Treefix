# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.random.randn(6, 4),
    index=list(string.ascii_letters[:6]),
    columns=["one", "two", "three", "four"],
)

_check_plot_works(df.plot.bar)
_check_plot_works(df.plot.bar, legend=False)
_check_plot_works(df.plot.bar, default_axes=True, subplots=True)
_check_plot_works(df.plot.bar, stacked=True)

df = DataFrame(
    np.random.randn(10, 15),
    index=list(string.ascii_letters[:10]),
    columns=range(15),
)
_check_plot_works(df.plot.bar)

df = DataFrame({"a": [0, 1], "b": [1, 0]})
ax = _check_plot_works(df.plot.bar)
self._check_ticks_props(ax, xrot=90)

ax = df.plot.bar(rot=35, fontsize=10)
self._check_ticks_props(ax, xrot=35, xlabelsize=10, ylabelsize=10)

ax = _check_plot_works(df.plot.barh)
self._check_ticks_props(ax, yrot=0)

ax = df.plot.barh(rot=55, fontsize=11)
self._check_ticks_props(ax, yrot=55, ylabelsize=11, xlabelsize=11)
