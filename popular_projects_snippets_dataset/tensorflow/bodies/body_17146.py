# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [10, 10, 10]
x = np.random.uniform(size=x_shape)
offset_height, offset_width = [0, 0]
self._assertReturns(x, x_shape, offset_height, offset_width, x, x_shape)
