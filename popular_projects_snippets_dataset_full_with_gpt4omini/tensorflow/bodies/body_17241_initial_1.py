import numpy as np # pragma: no cover

class Mock:  # pragma: no cover
    def _assertReturns(self, x, x_shape, y, y_shape): # pragma: no cover
        assert np.array(x).shape == tuple(x_shape) # pragma: no cover
        assert np.array(y).shape == tuple(y_shape) # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Crop even along col.
from l3.Runtime import _l_
x = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(7999)
x_shape = [2, 4, 1]
_l_(8000)

y = [2, 3, 6, 7]
_l_(8001)
y_shape = [2, 2, 1]
_l_(8002)

self._assertReturns(x, x_shape, y, y_shape)
_l_(8003)

# Crop odd along col.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
_l_(8004)
x_shape = [2, 6, 1]
_l_(8005)

y = [2, 3, 4, 8, 9, 10]
_l_(8006)
y_shape = [2, 3, 1]
_l_(8007)

self._assertReturns(x, x_shape, y, y_shape)
_l_(8008)

# Crop even along row.
x = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(8009)
x_shape = [4, 2, 1]
_l_(8010)

y = [3, 4, 5, 6]
_l_(8011)
y_shape = [2, 2, 1]
_l_(8012)

self._assertReturns(x, x_shape, y, y_shape)
_l_(8013)

# Crop odd along row.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_l_(8014)
x_shape = [8, 2, 1]
_l_(8015)

y = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
_l_(8016)
y_shape = [5, 2, 1]
_l_(8017)

self._assertReturns(x, x_shape, y, y_shape)
_l_(8018)
