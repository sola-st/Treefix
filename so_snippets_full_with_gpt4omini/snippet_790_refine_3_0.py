options = lambda **kwargs: None # pragma: no cover

options = lambda **kwargs: figsize(kwargs.get('repr.plot.width', 4), kwargs.get('repr.plot.height', 3)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

