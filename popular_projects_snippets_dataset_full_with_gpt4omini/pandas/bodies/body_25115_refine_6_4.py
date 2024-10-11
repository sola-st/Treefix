style = 'The sky is blue and the grass is green.' # pragma: no cover

style = 'rgb' # pragma: no cover
BASE_COLORS = {'r': '#ff0000', 'g': '#00ff00', 'b': '#0000ff'} # pragma: no cover

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
