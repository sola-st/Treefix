class MockOptions:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.repr = MockRepr() # pragma: no cover
 # pragma: no cover
class MockRepr: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.plot = MockPlot() # pragma: no cover
 # pragma: no cover
class MockPlot: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.width = 4 # pragma: no cover
        self.height = 3 # pragma: no cover
 # pragma: no cover
options = MockOptions() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

