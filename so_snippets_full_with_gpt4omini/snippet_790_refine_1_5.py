from types import SimpleNamespace # pragma: no cover

options = SimpleNamespace() # pragma: no cover
options.repr = SimpleNamespace() # pragma: no cover
options.repr.plot = SimpleNamespace() # pragma: no cover
options.repr.plot.width = 4 # pragma: no cover
options.repr.plot.height = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

