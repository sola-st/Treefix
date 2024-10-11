def options(*args, **kwargs):# pragma: no cover
    if 'repr.plot.width' in kwargs and 'repr.plot.height' in kwargs:# pragma: no cover
        plt.rcParams['figure.figsize'] = (kwargs['repr.plot.width'], kwargs['repr.plot.height']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(11834)

