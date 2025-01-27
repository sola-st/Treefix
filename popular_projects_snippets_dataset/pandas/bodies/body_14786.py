# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 19699: tests list-like y and verifies lbls & colors
df = DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
_check_plot_works(df.plot, x="A", y=y, label=lbl)

ax = df.plot(x=x, y=y, label=lbl, color=colors)
assert len(ax.lines) == len(y)
self._check_colors(ax.get_lines(), linecolors=colors)
