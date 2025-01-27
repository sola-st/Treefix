# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
from pandas.plotting._matplotlib.style import get_standard_colors

# Make sure the default color_types returns the specified amount
color1 = get_standard_colors(1, color_type="default")
color2 = get_standard_colors(9, color_type="default")
color3 = get_standard_colors(20, color_type="default")
assert len(color1) == 1
assert len(color2) == 9
assert len(color3) == 20
