# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Pad along row but crop along col.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 0, 2, 3, 6, 7, 0, 0]
y_shape = [4, 2, 1]

self._assertReturns(x, x_shape, y, y_shape)

# Crop along row but pad along col.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [4, 2, 1]

y = [0, 3, 4, 0, 0, 5, 6, 0]
y_shape = [2, 4, 1]

self._assertReturns(x, x_shape, y, y_shape)
