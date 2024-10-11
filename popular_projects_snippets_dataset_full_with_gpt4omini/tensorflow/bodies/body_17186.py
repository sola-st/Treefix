# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [100, 100, 10]
x = np.random.uniform(size=x_shape)

self._assertResizeCheckShape(x, x_shape, [150, 200], [150, 150, 10])
