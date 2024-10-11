matplotlib = types.ModuleType('matplotlib') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
from l3.Runtime import _l_
fig = matplotlib.pyplot.gcf()
_l_(12415)
fig.set_size_inches(18.5, 10.5)
_l_(12416)
fig.savefig('test2png.png', dpi=100)
_l_(12417)

fig.set_size_inches(18.5, 10.5, forward=True)
_l_(12418)

fig.set_dpi(100)
_l_(12419)

