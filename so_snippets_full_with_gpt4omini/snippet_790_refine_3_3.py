options = lambda **kwargs: None # pragma: no cover

options = lambda *args, **kwargs: None # pragma: no cover
repr = type('mock_repr', (), {'plot': type('mock_plot', (), {'width': 0, 'height': 0})()})() # pragma: no cover
repr.plot.width = 4 # pragma: no cover
repr.plot.height = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

