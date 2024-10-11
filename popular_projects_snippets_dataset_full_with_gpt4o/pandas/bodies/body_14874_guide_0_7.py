import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

def _check_plot_works(plot_func, **kwargs): # pragma: no cover
    fig, ax = plt.subplots() # pragma: no cover
    plot_func(ax=ax, **kwargs) # pragma: no cover
    return ax # pragma: no cover
 # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_check_colors': lambda self, patches, facecolors: all(patch.get_facecolor() == facecolor for patch, facecolor in zip(patches, facecolors)) # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
