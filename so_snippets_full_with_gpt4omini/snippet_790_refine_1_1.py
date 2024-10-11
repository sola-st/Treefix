class Options: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.repr = self.Repr() # pragma: no cover
    class Repr: # pragma: no cover
        def __init__(self): # pragma: no cover
            self.plot = self.Plot() # pragma: no cover
        class Plot: # pragma: no cover
            def __init__(self): # pragma: no cover
                self.width = 4 # pragma: no cover
                self.height = 3 # pragma: no cover
options = Options() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

