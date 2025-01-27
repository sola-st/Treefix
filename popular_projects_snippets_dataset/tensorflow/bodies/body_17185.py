# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [10, 100, 100, 10]
x = np.random.uniform(size=x_shape)

self._assertResizeCheckShape(x, x_shape, [75, 50], [10, 50, 50, 10])
