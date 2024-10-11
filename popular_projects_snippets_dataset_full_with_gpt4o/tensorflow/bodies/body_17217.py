# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [299, 299, 3]
x = np.random.uniform(size=x_shape)

self._assertResizeCheckShape(x, x_shape, [320, 320], [320, 320, 3])
