import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

def _check_plot_works(plot_func, **kwargs): # pragma: no cover
    fig, ax = plt.subplots() # pragma: no cover
    plot_func(ax=ax, **kwargs) # pragma: no cover
    plt.close(fig) # pragma: no cover
    return ax # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def _check_colors(self, patches, facecolors): # pragma: no cover
        for patch, facecolor in zip(patches, facecolors): # pragma: no cover
            expected_color = plt.colors.to_rgba(facecolor) # pragma: no cover
            actual_color = patch.get_facecolor() # pragma: no cover
            assert actual_color == expected_color, f'Expected {expected_color}, got {actual_color}' # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
