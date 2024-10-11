style = 'rggb'  # A sample style string containing color letters 'r' (red) and 'g' (green)' # pragma: no cover

BASE_COLORS = {'r': '#FF0000', 'g': '#00FF00', 'b': '#0000FF', 'c': '#00FFFF', 'm': '#FF00FF', 'y': '#FFFF00', 'k': '#000000', 'w': '#FFFFFF'} # pragma: no cover
style = 'rggb'  # A sample style string containing color letters 'r' (red) and 'g' (green)' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
from l3.Runtime import _l_
"""
    Check if there is a color letter in the style string.
    """
try:
    from matplotlib.colors import BASE_COLORS
    _l_(10553)

except ImportError:
    pass
aux = not set(BASE_COLORS).isdisjoint(style)
_l_(10554)

exit(aux)
