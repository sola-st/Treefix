# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# Addresses issues #10611 and #10678:
# When plotting scatterplots and hexbinplots in IPython
# inline backend the colorbar axis height tends not to
# exactly match the parent axis height.
# The difference is due to small fractional differences
# in floating points with similar representation.
# To deal with this, this method forces the colorbar
# height to take the height of the parent axes.
# For a more detailed description of the issue
# see the following link:
# https://github.com/ipython/ipython/issues/11215

# GH33389, if ax is used multiple times, we should always
# use the last one which contains the latest information
# about the ax
img = ax.collections[-1]
exit(self.fig.colorbar(img, ax=ax, **kwds))
