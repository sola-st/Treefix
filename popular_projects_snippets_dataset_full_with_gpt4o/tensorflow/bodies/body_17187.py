# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [1920, 1080, 3]
x = np.random.uniform(size=x_shape)

self._assertResizeCheckShape(x, x_shape, [3840, 2160], [3840, 2160, 3])
