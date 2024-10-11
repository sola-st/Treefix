# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_shape = [3, 3, 1]

offset_height, offset_width = [1, 0]
y = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_shape = [4, 3, 1]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 1]
y = [0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9]
y_shape = [3, 4, 1]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 0]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]
y_shape = [4, 3, 1]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)

offset_height, offset_width = [0, 0]
y = [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0]
y_shape = [3, 4, 1]
self._assertReturns(x, x_shape, offset_height, offset_width, y, y_shape)
