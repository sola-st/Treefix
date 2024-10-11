self = type('Mock', (object,), {'_assertReturns': lambda self, x, x_shape, y, y_shape: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Crop even along col.
from l3.Runtime import _l_
x = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(20623)
x_shape = [2, 4, 1]
_l_(20624)

y = [2, 3, 6, 7]
_l_(20625)
y_shape = [2, 2, 1]
_l_(20626)

self._assertReturns(x, x_shape, y, y_shape)
_l_(20627)

# Crop odd along col.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
_l_(20628)
x_shape = [2, 6, 1]
_l_(20629)

y = [2, 3, 4, 8, 9, 10]
_l_(20630)
y_shape = [2, 3, 1]
_l_(20631)

self._assertReturns(x, x_shape, y, y_shape)
_l_(20632)

# Crop even along row.
x = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(20633)
x_shape = [4, 2, 1]
_l_(20634)

y = [3, 4, 5, 6]
_l_(20635)
y_shape = [2, 2, 1]
_l_(20636)

self._assertReturns(x, x_shape, y, y_shape)
_l_(20637)

# Crop odd along row.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_l_(20638)
x_shape = [8, 2, 1]
_l_(20639)

y = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
_l_(20640)
y_shape = [5, 2, 1]
_l_(20641)

self._assertReturns(x, x_shape, y, y_shape)
_l_(20642)
