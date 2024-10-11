import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

_check_plot_works = lambda plot_function, **kwargs: plot_function().get_figure() # pragma: no cover
Series = pd.Series # pragma: no cover
self = type('Mock', (), {'_check_colors': lambda self, patches, facecolors: [patch.set_facecolor(fc) for patch, fc in zip(patches, facecolors)]})() # pragma: no cover

import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

_check_plot_works = lambda plot_func, **kwargs: plot_func() or plt.gca() # pragma: no cover
Series = pd.Series # pragma: no cover
self = type('Mock', (object,), {'_check_colors': MagicMock()})() # pragma: no cover
np.random = np.random # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(5072)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(5073)
