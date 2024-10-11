# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
scatter_matrix = plotting.scatter_matrix

ax = None
if pass_axis:
    _, ax = self.plt.subplots(3, 3)

with tm.RNGContext(42):
    df = DataFrame(np.random.randn(100, 3))

# we are plotting multiples on a sub-plot
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        scatter_matrix,
        frame=df,
        range_padding=0.1,
        ax=ax,
    )
axes0_labels = axes[0][0].yaxis.get_majorticklabels()

# GH 5662
expected = ["-2", "0", "2"]
self._check_text_labels(axes0_labels, expected)
self._check_ticks_props(axes, xlabelsize=8, xrot=90, ylabelsize=8, yrot=0)

df[0] = (df[0] - 2) / 3

# we are plotting multiples on a sub-plot
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(
        scatter_matrix,
        frame=df,
        range_padding=0.1,
        ax=ax,
    )
axes0_labels = axes[0][0].yaxis.get_majorticklabels()
expected = ["-1.0", "-0.5", "0.0"]
self._check_text_labels(axes0_labels, expected)
self._check_ticks_props(axes, xlabelsize=8, xrot=90, ylabelsize=8, yrot=0)
