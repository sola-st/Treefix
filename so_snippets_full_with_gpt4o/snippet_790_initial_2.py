from IPython.core.display import display # pragma: no cover
from IPython.display import set_matplotlib_formats # pragma: no cover

def options(**kwargs): # pragma: no cover
    for key, value in kwargs.items(): # pragma: no cover
        print(f"Setting {key} to {value}") # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(11834)

