import os # pragma: no cover

os.makedirs('path/to/save/image/to', exist_ok=True) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(2155)

except ImportError:
    pass
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
_l_(2156)  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
_l_(2157)
fig.savefig('path/to/save/image/to.png')   # save the figure to file
_l_(2158)   # save the figure to file
plt.close(fig)    # close the figure window
_l_(2159)    # close the figure window

