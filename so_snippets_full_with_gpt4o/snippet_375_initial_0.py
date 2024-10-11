import numpy as np # pragma: no cover
import matplotlib.pyplot as plt # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis
# Note the super cluttered ticks on both X and Y axis.

# inputs
from l3.Runtime import _l_
x = np.arange(1, 101)
_l_(14537)
y = x * np.log(x) 
_l_(14538) 

fig = plt.figure()     # create figure
_l_(14539)     # create figure
ax = fig.add_subplot(111)
_l_(14540)
ax.plot(x, y)
_l_(14541)
ax.set_xticks(x)        # set xtick values
_l_(14542)        # set xtick values
ax.set_yticks(y)        # set ytick values
_l_(14543)        # set ytick values

plt.show()
_l_(14544)

# inputs
x = np.arange(1, 101)
_l_(14545)
y = x * np.log(x)
_l_(14546)

fig = plt.figure()       # create figure
_l_(14547)       # create figure
ax = fig.add_subplot(111)
_l_(14548)
ax.plot(x, y)
_l_(14549)

ax.set_xticks(x)
_l_(14550)
ax.set_yticks(y)
_l_(14551)

# which values need to be shown?
# here, we show every third value from `x` and `y`
show_every = 3
_l_(14552)

sparse_xticks = [None] * x.shape[0]
_l_(14553)
sparse_xticks[::show_every] = x[::show_every]
_l_(14554)

sparse_yticks = [None] * y.shape[0]
_l_(14555)
sparse_yticks[::show_every] = y[::show_every]
_l_(14556)

ax.set_xticklabels(sparse_xticks, fontsize=6)   # set sparse xtick values
_l_(14557)   # set sparse xtick values
ax.set_yticklabels(sparse_yticks, fontsize=6)   # set sparse ytick values
_l_(14558)   # set sparse ytick values

plt.show()
_l_(14559)

