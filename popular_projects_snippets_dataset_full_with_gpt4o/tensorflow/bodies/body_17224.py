# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Reduce vertical dimension
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 1, 3, 0]
y_shape = [1, 4, 1]

self._assertReturns(x, x_shape, y, y_shape)

# Reduce horizontal dimension
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [1, 3, 0, 0]
y_shape = [2, 2, 1]

self._assertReturns(x, x_shape, y, y_shape)

x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [1, 3]
y_shape = [1, 2, 1]

self._assertReturns(x, x_shape, y, y_shape)
