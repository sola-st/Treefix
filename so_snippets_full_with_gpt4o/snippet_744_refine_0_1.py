import sys # pragma: no cover
import types # pragma: no cover

matplotlib = types.ModuleType('matplotlib') # pragma: no cover
sys.modules['matplotlib'] = matplotlib # pragma: no cover
matplotlib.pyplot = types.ModuleType('matplotlib.pyplot') # pragma: no cover
sys.modules['matplotlib.pyplot'] = matplotlib.pyplot # pragma: no cover
matplotlib.pyplot.plot = lambda *args, **kwargs: None # pragma: no cover
matplotlib.pyplot.xlabel = lambda *args, **kwargs: None # pragma: no cover
matplotlib.pyplot.subplot = lambda *args, **kwargs: type('Mock', (object,), {'plot': lambda self, *args, **kwargs: None, 'set_xlabel': lambda self, *args, **kwargs: None})() # pragma: no cover
ax = matplotlib.pyplot.subplot() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(12867)

except ImportError:
    pass

# global state version - modifies "current" figure
plt.plot(...)
_l_(12868)
plt.xlabel(...)
_l_(12869)

# axes version - modifies explicit axes
ax.plot(...)
_l_(12870)
ax.set_xlabel(...)
_l_(12871)

