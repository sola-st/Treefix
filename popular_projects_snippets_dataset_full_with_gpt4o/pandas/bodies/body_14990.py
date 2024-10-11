# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_misc.py
# GH17525
df = DataFrame(np.zeros((10, 10)))

# Make sure that the np.random.seed isn't reset by get_standard_colors
plotting.parallel_coordinates(df, 0)
rand1 = np.random.random()
plotting.parallel_coordinates(df, 0)
rand2 = np.random.random()
assert rand1 != rand2

# Make sure it produces the same colors every time it's called
from pandas.plotting._matplotlib.style import get_standard_colors

color1 = get_standard_colors(1, color_type="random")
color2 = get_standard_colors(1, color_type="random")
assert color1 == color2
