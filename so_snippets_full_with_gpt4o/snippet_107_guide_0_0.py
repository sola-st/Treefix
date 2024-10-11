import sys # pragma: no cover
import types # pragma: no cover

sys.modules['matplotlib'] = types.ModuleType('matplotlib') # pragma: no cover
matplotlib = sys.modules['matplotlib'] # pragma: no cover
sys.modules['matplotlib.pyplot'] = types.ModuleType('matplotlib.pyplot') # pragma: no cover
matplotlib.pyplot = sys.modules['matplotlib.pyplot'] # pragma: no cover
def subplots(nrows=1, ncols=1): return type('MockFig', (object,), {'savefig': lambda self, path: print('Figure saved to', path), 'close': lambda self: print('Figure closed')})(), type('MockAx', (object,), {'plot': lambda self, *args: print('Plot created with data:', args)})() # pragma: no cover
matplotlib.pyplot.subplots = subplots # pragma: no cover
matplotlib.pyplot.close = lambda fig: fig.close() # pragma: no cover

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

