import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

_check_plot_works = lambda plot_func, **kwargs: plot_func(**kwargs) # pragma: no cover
Series = pd.Series # pragma: no cover
np_random_mock = type('Mock', (object,), {'randn': np.random.randn}) # pragma: no cover
np = type('Mock', (object,), {'random': np_random_mock()}) # pragma: no cover
self = type('Mock', (object,), {'_check_colors': lambda patches, facecolors: None})() # pragma: no cover

import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

_check_plot_works = lambda plot_func, **kwargs: plot_func(**kwargs).figure.axes[0] # pragma: no cover
self = type('Mock', (object,), {'_check_colors': lambda self, patches, facecolors: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
