class options: pass # pragma: no cover
options.repr = type('Mock', (object,), {})() # pragma: no cover
options.repr.plot = type('Mock', (object,), {'width': 0, 'height': 0})() # pragma: no cover
options.repr.plot.width = 4 # pragma: no cover
options.repr.plot.height = 3 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

