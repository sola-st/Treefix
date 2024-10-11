# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [10, 10, 10]
x = np.random.uniform(size=x_shape)

self._assertReturns(x, x_shape, x, x_shape)
