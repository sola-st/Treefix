# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(14345)

except ImportError:
    pass
fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
_l_(14346)  # create figure & 1 axis
ax.plot([0,1,2], [10,20,3])
_l_(14347)
fig.savefig('path/to/save/image/to.png')   # save the figure to file
_l_(14348)   # save the figure to file
plt.close(fig)    # close the figure window
_l_(14349)    # close the figure window

