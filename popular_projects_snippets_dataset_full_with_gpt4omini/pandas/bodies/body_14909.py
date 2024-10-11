# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from pandas.plotting._matplotlib.style import get_standard_colors

result = get_standard_colors(1, color=c)
assert result == [c]

result = get_standard_colors(1, color=[c])
assert result == [c]

result = get_standard_colors(3, color=c)
assert result == [c] * 3

result = get_standard_colors(3, color=[c])
assert result == [c] * 3
