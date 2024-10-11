import matplotlib.pyplot as plt # pragma: no cover
import numpy as np # pragma: no cover

x = np.arange(0, 10, 0.1) # pragma: no cover
y = np.sin(x) # pragma: no cover
fig, ax = plt.subplots() # pragma: no cover
plt.plot(x, y) # pragma: no cover
plt.xlabel('X-axis') # pragma: no cover
ax.plot(x, y) # pragma: no cover
ax.set_xlabel('X-axis on Axes') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(3297)

except ImportError:
    pass

# global state version - modifies "current" figure
plt.plot(...)
_l_(3298)
plt.xlabel(...)
_l_(3299)

# axes version - modifies explicit axes
ax.plot(...)
_l_(3300)
ax.set_xlabel(...)
_l_(3301)

