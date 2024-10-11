import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

_check_plot_works = lambda plot_function, color: plot_function(color=color) # pragma: no cover
Series = pd.Series # pragma: no cover
self = type('Mock', (object,), {'_check_colors': lambda patches, facecolors: None})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

_check_plot_works = lambda plot_func, color: plot_func(color=color).figure.gca() # pragma: no cover
Series = pd.Series # pragma: no cover
self = type('Mock', (object,), {'_check_colors': lambda self, patches, facecolors: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
