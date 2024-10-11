# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
from l3.Runtime import _l_
ax = _check_plot_works(Series(np.random.randn(10)).plot.bar, color="black")
_l_(5072)
self._check_colors([ax.patches[0]], facecolors=["black"])
_l_(5073)
