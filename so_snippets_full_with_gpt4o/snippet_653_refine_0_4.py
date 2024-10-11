import numpy as np # pragma: no cover

import numpy as np # pragma: no cover
import numpy.typing as npt # pragma: no cover

image = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
from l3.Runtime import _l_
def find_nearest(array, values):
    _l_(12063)

    array = np.asarray(array)
    _l_(12059)

    # the last dim must be 1 to broadcast in (array - values) below.
    values = np.expand_dims(values, axis=-1) 
    _l_(12060) 

    indices = np.abs(array - values).argmin(axis=-1)
    _l_(12061)
    aux = array[indices]
    _l_(12062)

    return aux


image = plt.imread('example_3_band_image.jpg')
_l_(12064)

print(image.shape) # should be (nrows, ncols, 3)
_l_(12065) # should be (nrows, ncols, 3)

quantiles = np.linspace(0, 255, num=2 ** 2, dtype=np.uint8)
_l_(12066)

quantiled_image = find_nearest(quantiles, image)
_l_(12067)

print(quantiled_image.shape) # should be (nrows, ncols, 3)
_l_(12068) # should be (nrows, ncols, 3)

