# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-the-x-or-y-axis
# Note the super cluttered ticks on both X and Y axis.

# inputs
from l3.Runtime import _l_
x = np.arange(1, 101)
_l_(2777)
y = x * np.log(x) 
_l_(2778) 

fig = plt.figure()     # create figure
_l_(2779)     # create figure
ax = fig.add_subplot(111)
_l_(2780)
ax.plot(x, y)
_l_(2781)
ax.set_xticks(x)        # set xtick values
_l_(2782)        # set xtick values
ax.set_yticks(y)        # set ytick values
_l_(2783)        # set ytick values

plt.show()
_l_(2784)

# inputs
x = np.arange(1, 101)
_l_(2785)
y = x * np.log(x)
_l_(2786)

fig = plt.figure()       # create figure
_l_(2787)       # create figure
ax = fig.add_subplot(111)
_l_(2788)
ax.plot(x, y)
_l_(2789)

ax.set_xticks(x)
_l_(2790)
ax.set_yticks(y)
_l_(2791)

# which values need to be shown?
# here, we show every third value from `x` and `y`
show_every = 3
_l_(2792)

sparse_xticks = [None] * x.shape[0]
_l_(2793)
sparse_xticks[::show_every] = x[::show_every]
_l_(2794)

sparse_yticks = [None] * y.shape[0]
_l_(2795)
sparse_yticks[::show_every] = y[::show_every]
_l_(2796)

ax.set_xticklabels(sparse_xticks, fontsize=6)   # set sparse xtick values
_l_(2797)   # set sparse xtick values
ax.set_yticklabels(sparse_yticks, fontsize=6)   # set sparse ytick values
_l_(2798)   # set sparse ytick values

plt.show()
_l_(2799)

