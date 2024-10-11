import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas import Series # pragma: no cover

def _check_plot_works(func, **kwargs): # pragma: no cover
    fig, ax = plt.subplots() # pragma: no cover
    func(**kwargs) # pragma: no cover
    return ax # pragma: no cover
 # pragma: no cover
class Mock(object): # pragma: no cover
    def _check_colors(self, patches, facecolors): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
