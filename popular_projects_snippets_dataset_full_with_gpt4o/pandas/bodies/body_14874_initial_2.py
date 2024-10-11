import numpy as np # pragma: no cover
from pandas import Series # pragma: no cover

_check_plot_works = lambda func, **kwargs: func(**kwargs) # pragma: no cover
class MockSelf(object):# pragma: no cover
    def _check_colors(self, patches, facecolors):# pragma: no cover
        pass# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(16746)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(16747)
