from IPython.core.display import set_matplotlib_formats # pragma: no cover

def options(*args): # pragma: no cover
    set_matplotlib_formats('png') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(11834)

