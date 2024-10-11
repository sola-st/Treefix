import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1111)

except ImportError:
    pass

# x coordinates for the lines
xcoords = [0.1, 0.3, 0.5]
_l_(1112)
# colors for the lines
colors = ['r','k','b']
_l_(1113)

for xc,c in zip(xcoords,colors):
    _l_(1115)

    plt.axvline(x=xc, label='line at x = {}'.format(xc), c=c)
    _l_(1114)

plt.legend()
_l_(1116)
plt.show()
_l_(1117)

