import numpy as np # pragma: no cover

plt = type('Mock', (object,), {'imread': lambda path: np.zeros((10, 10, 3), dtype=np.uint8)})() # pragma: no cover
np = type('Mock', (object,), {'asarray': np.asarray, 'expand_dims': np.expand_dims, 'abs': np.abs, 'linspace': np.linspace, 'uint8': np.uint8})() # pragma: no cover

import numpy as np # pragma: no cover

plt = type('Mock', (object,), {'imread': lambda path: np.zeros((100, 100, 3), dtype=np.uint8)})() # pragma: no cover
np = type('Mock', (object,), {'asarray': staticmethod(np.asarray), 'expand_dims': staticmethod(np.expand_dims), 'abs': staticmethod(np.abs), 'linspace': staticmethod(np.linspace), 'uint8': np.uint8})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
from l3.Runtime import _l_
def find_nearest(array, values):
    _l_(350)

    array = np.asarray(array)
    _l_(346)

    # the last dim must be 1 to broadcast in (array - values) below.
    values = np.expand_dims(values, axis=-1) 
    _l_(347) 

    indices = np.abs(array - values).argmin(axis=-1)
    _l_(348)
    aux = array[indices]
    _l_(349)

    return aux


image = plt.imread('example_3_band_image.jpg')
_l_(351)

print(image.shape) # should be (nrows, ncols, 3)
_l_(352) # should be (nrows, ncols, 3)

quantiles = np.linspace(0, 255, num=2 ** 2, dtype=np.uint8)
_l_(353)

quantiled_image = find_nearest(quantiles, image)
_l_(354)

print(quantiled_image.shape) # should be (nrows, ncols, 3)
_l_(355) # should be (nrows, ncols, 3)

