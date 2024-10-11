import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

_check_plot_works = lambda x, color: x(color=color) # pragma: no cover
class MockSelfObject(object):# pragma: no cover
    def _check_colors(self, patches, facecolors):# pragma: no cover
        pass# pragma: no cover
self = MockSelfObject() # pragma: no cover

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
