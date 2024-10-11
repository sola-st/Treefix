def options(*args, **kwargs): # pragma: no cover
    for arg in args: # pragma: no cover
        if arg == 'repr.plot.width==4': # pragma: no cover
            plt.rcParams['figure.figsize'] = (4, plt.rcParams['figure.figsize'][1]) # pragma: no cover
        elif arg == 'repr.plot.height==3': # pragma: no cover
            plt.rcParams['figure.figsize'] = (plt.rcParams['figure.figsize'][0], 3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(11834)

