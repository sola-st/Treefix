# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH 38969
# Ensure IntervalIndex x-axis produces a bar plot as expected
from matplotlib.text import Text

expected = [Text(0, 0, "([0, 1],)"), Text(1, 0, "([1, 2],)")]
s = Series(
    [1, 2],
    index=[interval_range(0, 2, closed="both")],
)
_check_plot_works(s.plot.bar)
assert all(
    (a.get_text() == b.get_text())
    for a, b in zip(s.plot.bar().get_xticklabels(), expected)
)
