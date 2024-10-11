# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH20726

# Make sure not to add more colors so that matplotlib can cycle
# correctly.
from matplotlib import cm

from pandas.plotting._matplotlib.style import get_standard_colors

color_before = cm.gnuplot(range(5))
color_after = get_standard_colors(1, color=color_before)
assert len(color_after) == len(color_before)

df = DataFrame(np.random.randn(48, 4), columns=list("ABCD"))

color_list = cm.gnuplot(np.linspace(0, 1, 16))
p = df.A.plot.bar(figsize=(16, 7), color=color_list)
assert p.patches[1].get_facecolor() == p.patches[17].get_facecolor()
