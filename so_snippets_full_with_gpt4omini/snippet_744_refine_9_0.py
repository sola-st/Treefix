import matplotlib.pyplot as plt # pragma: no cover
import numpy as np # pragma: no cover

ax = plt.subplot() # pragma: no cover
plt.plot(np.random.rand(10), np.random.rand(10)) # pragma: no cover
plt.xlabel('X-axis label') # pragma: no cover
ax.plot(np.random.rand(10), np.random.rand(10)) # pragma: no cover
ax.set_xlabel('Y-axis label') # pragma: no cover

import matplotlib.pyplot as plt # pragma: no cover
import numpy as np # pragma: no cover

ax = plt.subplot() # pragma: no cover
x = np.linspace(0, 10, 100) # pragma: no cover
y = np.sin(x) # pragma: no cover
plt.plot(x, y, label='Sine Wave') # pragma: no cover
plt.xlabel('X-axis') # pragma: no cover
ax.plot(x, y, label='Sine Wave') # pragma: no cover
ax.set_xlabel('X-axis') # pragma: no cover

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

