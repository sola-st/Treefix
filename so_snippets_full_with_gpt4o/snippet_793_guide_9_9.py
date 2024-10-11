import matplotlib.pyplot as plt # pragma: no cover

class MockScatter: # pragma: no cover
    @staticmethod # pragma: no cover
    def annotate(txt, xy): pass # pragma: no cover
mock_scatter_instance = MockScatter() # pragma: no cover
fig, ax = None, mock_scatter_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(15191)

except ImportError:
    pass
y = [2.56422, 3.77284, 3.52623, 3.51468, 3.02199]
_l_(15192)
z = [0.15, 0.3, 0.45, 0.6, 0.75]
_l_(15193)
n = [58, 651, 393, 203, 123]
_l_(15194)

fig, ax = plt.scatter(z, y)
_l_(15195)

for i, txt in enumerate(n):
    _l_(15197)

    ax.annotate(txt, (z[i], y[i]))
    _l_(15196)
try:
    import matplotlib.pyplot as plt
    _l_(15199)

except ImportError:
    pass
plt.scatter(z, y)
_l_(15200)

for i, txt in enumerate(n):
    _l_(15202)

    plt.annotate(txt, (z[i], y[i]))
    _l_(15201)

