from IPython.core.display import display # pragma: no cover
from IPython.core.interactiveshell import InteractiveShell # pragma: no cover

def options(width, height): # pragma: no cover
    InteractiveShell.instance().plot_options = {'width': width, 'height': height} # pragma: no cover

from IPython.core.display import display # pragma: no cover
from IPython.core.interactiveshell import InteractiveShell # pragma: no cover

class repr: # pragma: no cover
    class plot: # pragma: no cover
        width = 4 # pragma: no cover
        height = 3 # pragma: no cover
def options(width, height): # pragma: no cover
    InteractiveShell.instance().plot_options = {'width': width, 'height': height} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(11834)

