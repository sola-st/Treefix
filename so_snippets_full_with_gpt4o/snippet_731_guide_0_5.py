import numpy as np # pragma: no cover

class MockImportError(Exception): # pragma: no cover
    pass # pragma: no cover
try: # pragma: no cover
except MockImportError: # pragma: no cover
    pass # pragma: no cover
    if name == 'matplotlib.pyplot': # pragma: no cover
        raise ImportError # pragma: no cover
    return patch.get_original(name) # pragma: no cover
    try: # pragma: no cover
    except ImportError: # pragma: no cover
        pass # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(13501)

except ImportError:
    pass

# x coordinates for the lines
xcoords = [0.1, 0.3, 0.5]
_l_(13502)
# colors for the lines
colors = ['r','k','b']
_l_(13503)

for xc,c in zip(xcoords,colors):
    _l_(13505)

    plt.axvline(x=xc, label='line at x = {}'.format(xc), c=c)
    _l_(13504)

plt.legend()
_l_(13506)
plt.show()
_l_(13507)

