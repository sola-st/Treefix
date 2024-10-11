from matplotlib.colors import BASE_COLORS # pragma: no cover

style = 'Solid'  # Example string that does not contain base colors from matplotlib # pragma: no cover
# Alternatively, if the goal is to match a color, another example could be: # pragma: no cover
# style = 'blue'  # Where 'blue' is a color present in BASE_COLORS # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
from l3.Runtime import _l_
"""
    Check if there is a color letter in the style string.
    """
try:
    from matplotlib.colors import BASE_COLORS
    _l_(21934)

except ImportError:
    pass
aux = not set(BASE_COLORS).isdisjoint(style)
_l_(21935)

exit(aux)
