class Options:# pragma: no cover
    def __init__(self, width, height):# pragma: no cover
        self.repr = type("Repr", (), {"plot": type("Plot", (), {"width": width, "height": height})()})()# pragma: no cover
options = Options(4, 3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36367986/how-to-make-inline-plots-in-jupyter-notebook-larger
from l3.Runtime import _l_
options(repr.plot.width==4, repr.plot.height==3)
_l_(1)

