# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
from l3.Runtime import _l_
for i in range(5):
    _l_(15238)

    fig = plot_figure()
    _l_(15236)
    plt.close(fig)
    _l_(15237)
# This returns a list with all figure numbers available
print(plt.get_fignums())
_l_(15239)

for i in range(5):
    _l_(15242)

    fig = plot_figure()
    _l_(15240)
    fig.clf()
    _l_(15241)
# This returns a list with all figure numbers available
print(plt.get_fignums())
_l_(15243)
try:
    import numpy as np
    _l_(15245)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(15247)

except ImportError:
    pass
x = np.arange(1000)
_l_(15248)
y = np.sin(x)
_l_(15249)

for i in range(5):
    _l_(15254)

    fig = plt.figure()
    _l_(15250)
    ax = fig.add_subplot(1, 1, 1)
    _l_(15251)
    ax.plot(x, y)
    _l_(15252)
    plt.close(fig)
    _l_(15253)

print(plt.get_fignums())
_l_(15255)

for i in range(5):
    _l_(15260)

    fig = plt.figure()
    _l_(15256)
    ax = fig.add_subplot(1, 1, 1)
    _l_(15257)
    ax.plot(x, y)
    _l_(15258)
    fig.clf()
    _l_(15259)

print(plt.get_fignums())
_l_(15261)

