# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = tm.makeTimeDataFrame()
_check_plot_works(df.plot, grid=False)

# _check_plot_works adds an ax so use default_axes=True to avoid warning
axes = _check_plot_works(df.plot, default_axes=True, subplots=True)
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

axes = _check_plot_works(
    df.plot,
    default_axes=True,
    subplots=True,
    layout=(-1, 2),
)
self._check_axes_shape(axes, axes_num=4, layout=(2, 2))

axes = _check_plot_works(
    df.plot,
    default_axes=True,
    subplots=True,
    use_index=False,
)
self._check_ticks_props(axes, xrot=0)
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

df = DataFrame({"x": [1, 2], "y": [3, 4]})
msg = "'Line2D' object has no property 'blarg'"
with pytest.raises(AttributeError, match=msg):
    df.plot.line(blarg=True)

df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))

ax = _check_plot_works(df.plot, use_index=True)
self._check_ticks_props(ax, xrot=0)
_check_plot_works(df.plot, yticks=[1, 5, 10])
_check_plot_works(df.plot, xticks=[1, 5, 10])
_check_plot_works(df.plot, ylim=(-100, 100), xlim=(-100, 100))

_check_plot_works(df.plot, default_axes=True, subplots=True, title="blah")

# We have to redo it here because _check_plot_works does two plots,
# once without an ax kwarg and once with an ax kwarg and the new sharex
# behaviour does not remove the visibility of the latter axis (as ax is
# present).  see: https://github.com/pandas-dev/pandas/issues/9737

axes = df.plot(subplots=True, title="blah")
self._check_axes_shape(axes, axes_num=3, layout=(3, 1))
# axes[0].figure.savefig("test.png")
for ax in axes[:2]:
    self._check_visible(ax.xaxis)  # xaxis must be visible for grid
    self._check_visible(ax.get_xticklabels(), visible=False)
    self._check_visible(ax.get_xticklabels(minor=True), visible=False)
    self._check_visible([ax.xaxis.get_label()], visible=False)
for ax in [axes[2]]:
    self._check_visible(ax.xaxis)
    self._check_visible(ax.get_xticklabels())
    self._check_visible([ax.xaxis.get_label()])
    self._check_ticks_props(ax, xrot=0)

_check_plot_works(df.plot, title="blah")

tuples = zip(string.ascii_letters[:10], range(10))
df = DataFrame(np.random.rand(10, 3), index=MultiIndex.from_tuples(tuples))
ax = _check_plot_works(df.plot, use_index=True)
self._check_ticks_props(ax, xrot=0)

# unicode
index = MultiIndex.from_tuples(
    [
        ("\u03b1", 0),
        ("\u03b1", 1),
        ("\u03b2", 2),
        ("\u03b2", 3),
        ("\u03b3", 4),
        ("\u03b3", 5),
        ("\u03b4", 6),
        ("\u03b4", 7),
    ],
    names=["i0", "i1"],
)
columns = MultiIndex.from_tuples(
    [("bar", "\u0394"), ("bar", "\u0395")], names=["c0", "c1"]
)
df = DataFrame(np.random.randint(0, 10, (8, 2)), columns=columns, index=index)
_check_plot_works(df.plot, title="\u03A3")

# GH 6951
# Test with single column
df = DataFrame({"x": np.random.rand(10)})
axes = _check_plot_works(df.plot.bar, subplots=True)
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))

axes = _check_plot_works(df.plot.bar, subplots=True, layout=(-1, 1))
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
# When ax is supplied and required number of axes is 1,
# passed ax should be used:
fig, ax = self.plt.subplots()
axes = df.plot.bar(subplots=True, ax=ax)
assert len(axes) == 1
result = ax.axes
assert result is axes[0]
