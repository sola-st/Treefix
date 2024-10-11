x_values = [0, 1, 2, 3, 4] # pragma: no cover
y_values = [0, 1, 4, 9, 16] # pragma: no cover
label_x_axis = 'X-Axis Label' # pragma: no cover

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

