# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Pad even along col.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 1, 2, 3, 4, 0, 0, 5, 6, 7, 8, 0]
y_shape = [2, 6, 1]

self._assertReturns(x, x_shape, y, y_shape)

# Pad odd along col.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 1, 2, 3, 4, 0, 0, 0, 5, 6, 7, 8, 0, 0]
y_shape = [2, 7, 1]

self._assertReturns(x, x_shape, y, y_shape)

# Pad even along row.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0]
y_shape = [4, 4, 1]

self._assertReturns(x, x_shape, y, y_shape)

# Pad odd along row.
x = [1, 2, 3, 4, 5, 6, 7, 8]
x_shape = [2, 4, 1]

y = [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0]
y_shape = [5, 4, 1]

self._assertReturns(x, x_shape, y, y_shape)
