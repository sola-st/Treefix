# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from matplotlib import colors

from pandas.plotting._matplotlib.style import get_standard_colors

# multiple colors like mediumaquamarine
for c in colors.cnames:
    result = get_standard_colors(num_colors=1, color=c)
    assert result == [c]

    result = get_standard_colors(num_colors=1, color=[c])
    assert result == [c]

    result = get_standard_colors(num_colors=3, color=c)
    assert result == [c] * 3

    result = get_standard_colors(num_colors=3, color=[c])
    assert result == [c] * 3

# single letter colors like k
for c in colors.ColorConverter.colors:
    result = get_standard_colors(num_colors=1, color=c)
    assert result == [c]

    result = get_standard_colors(num_colors=1, color=[c])
    assert result == [c]

    result = get_standard_colors(num_colors=3, color=c)
    assert result == [c] * 3

    result = get_standard_colors(num_colors=3, color=[c])
    assert result == [c] * 3
