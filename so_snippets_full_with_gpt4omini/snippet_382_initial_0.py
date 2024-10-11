import numpy as np # pragma: no cover
import matplotlib.pyplot as plt # pragma: no cover

def plot_figure(): return plt.figure() # pragma: no cover
plt = type('Mock', (object,), {'close': plt.close, 'get_fignums': plt.get_fignums, 'figure': plt.figure})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
from l3.Runtime import _l_
for i in range(5):
    _l_(3251)

    fig = plot_figure()
    _l_(3249)
    plt.close(fig)
    _l_(3250)
# This returns a list with all figure numbers available
print(plt.get_fignums())
_l_(3252)

for i in range(5):
    _l_(3255)

    fig = plot_figure()
    _l_(3253)
    fig.clf()
    _l_(3254)
# This returns a list with all figure numbers available
print(plt.get_fignums())
_l_(3256)
try:
    import numpy as np
    _l_(3258)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(3260)

except ImportError:
    pass
x = np.arange(1000)
_l_(3261)
y = np.sin(x)
_l_(3262)

for i in range(5):
    _l_(3267)

    fig = plt.figure()
    _l_(3263)
    ax = fig.add_subplot(1, 1, 1)
    _l_(3264)
    ax.plot(x, y)
    _l_(3265)
    plt.close(fig)
    _l_(3266)

print(plt.get_fignums())
_l_(3268)

for i in range(5):
    _l_(3273)

    fig = plt.figure()
    _l_(3269)
    ax = fig.add_subplot(1, 1, 1)
    _l_(3270)
    ax.plot(x, y)
    _l_(3271)
    fig.clf()
    _l_(3272)

print(plt.get_fignums())
_l_(3274)

