# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_shape = [3, 3, 1]

offset_height, offset_width = [1, 0]
y_shape = [2, 3, 1]
y = [4, 5, 6, 7, 8, 9]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 1]
y_shape = [3, 2, 1]
y = [2, 3, 5, 6, 8, 9]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 0]
y_shape = [2, 3, 1]
y = [1, 2, 3, 4, 5, 6]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 0]
y_shape = [3, 2, 1]
y = [1, 2, 4, 5, 7, 8]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)
