# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.abs(np.random.randn(5, 2)), index=range(5), columns=["x", "y"]
)
df_err = DataFrame(
    np.abs(np.random.randn(5, 2)) / 5, index=range(5), columns=["x", "y"]
)

ax = _check_plot_works(df.plot.scatter, x="x", y="y")
self._check_has_errorbars(ax, xerr=0, yerr=0)
ax = _check_plot_works(df.plot.scatter, x="x", y="y", xerr=df_err)
self._check_has_errorbars(ax, xerr=1, yerr=0)

ax = _check_plot_works(df.plot.scatter, x="x", y="y", yerr=df_err)
self._check_has_errorbars(ax, xerr=0, yerr=1)
ax = _check_plot_works(df.plot.scatter, x="x", y="y", xerr=df_err, yerr=df_err)
self._check_has_errorbars(ax, xerr=1, yerr=1)

def _check_errorbar_color(containers, expected, has_err="has_xerr"):
    lines = []
    errs = [c.lines for c in ax.containers if getattr(c, has_err, False)][0]
    for el in errs:
        if is_list_like(el):
            lines.extend(el)
        else:
            lines.append(el)
    err_lines = [x for x in lines if x in ax.collections]
    self._check_colors(
        err_lines, linecolors=np.array([expected] * len(err_lines))
    )

# GH 8081
df = DataFrame(
    np.abs(np.random.randn(10, 5)), columns=["a", "b", "c", "d", "e"]
)
ax = df.plot.scatter(x="a", y="b", xerr="d", yerr="e", c="red")
self._check_has_errorbars(ax, xerr=1, yerr=1)
_check_errorbar_color(ax.containers, "red", has_err="has_xerr")
_check_errorbar_color(ax.containers, "red", has_err="has_yerr")

ax = df.plot.scatter(x="a", y="b", yerr="e", color="green")
self._check_has_errorbars(ax, xerr=0, yerr=1)
_check_errorbar_color(ax.containers, "green", has_err="has_yerr")
